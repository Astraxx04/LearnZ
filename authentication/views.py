from django.views.decorators.csrf import csrf_exempt
from . tokens import generate_token
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from LearnZ import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
import django
from authentication import models
from django.utils.encoding import force_str
# import pyautogui
django.utils.encoding.force_text = force_str


# Create your views for students here.
def index(request):
    return render(request, "authentication/index.html")

def course(request):
    return render(request, "authentication/Course_Page.html")


def student_signup(request):
    if request.method == "POST":
        CollegeName = request.POST['CollegeName']
        username = request.POST['usn']
        fname = request.POST['FName']
        lname = request.POST['LName']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['ConfiPass']

        if models.Student.objects.filter(username=username):
            messages.error(request, 'USN already exist! Please try some other username.')
            return redirect('student_signup')

        if models.Student.objects.filter(email=email).exists():
            messages.error(request, 'Email Already Registered!!')
            return redirect('student_signup')

        if len(username) > 20:
            messages.error(request, 'USN must be under 20 characters!!')
            return redirect('student_signup')

        if pass1 != pass2:
            messages.error(request, "Passwords didn't match!!")
            return redirect('student_signup')

        if not username.isalnum():
            messages.error(request, 'Username must be Alpha-Numeric!!')
            return redirect('student_signup')

        myuser = models.Student.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        #myuser.CollegeName = CollegeName
        # myuser.last_name = lname
        # myuser.is_active = False
        #myuser.is_active = False
        myuser.save()
        # pyautogui.alert("Your Account has been created succesfully!!.")
        messages.success(request, 'User Created.')
        return redirect('student_signin')

    return render(request, "authentication/StudentSignup.html")

def teacher_signup(request):
    
    if request.method == "POST":
        CollegeName = request.POST['CollegeName']
        username = request.POST['teachid']
        fname = request.POST['FName']
        lname = request.POST['LName']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['ConfiPass']

        if models.Teacher.objects.filter(username=username):
            messages.error(request, 'teacherid already exist! Please try some other username.')
            return redirect('teacher_signup')

        if models.Teacher.objects.filter(email=email).exists():
            messages.error(request, 'Email Already Registered!!')
            return redirect('teacher_signin')

        if len(username) > 20:
            messages.error(request, 'USN must be under 20 characters!!')
            return redirect('teacher_signin')

        if pass1 != pass2:
            messages.error(request, "Passwords didn't match!!")
            return redirect('teacher_signin')

        if not username.isalnum():
            messages.error(request, 'Username must be Alpha-Numeric!!')
            return redirect('teacher_signin')

        myuser = models.Teacher.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        #myuser.CollegeName = CollegeName
        # myuser.last_name = lname
        # myuser.is_active = False
        #myuser.is_active = False
        myuser.save()
        messages.success(request, 'User Created.')
        return redirect('teacher_signin')

    return render(request, "authentication/TeacherSignup.html")


def student_signin(request):
    if request.method == 'POST':
        username = request.POST.get('usn',False)
        pass1 = request.POST.get('password','')
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            fname = user.first_name
            messages.success(request, 'Login Success')
            return render(request, "courses/Course_Page.html",{"fname":fname})
        else:
            messages.error(request, 'Recheck Credentials.')
            return render(request, "authentication/StudentLogin.html")

    return render(request, "authentication/StudentLogin.html")


def teacher_signin(request):
    if request.method == 'POST':
        username = request.POST.get('teachid',False)
        pass1 = request.POST.get('password','')
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            fname = user.first_name
            messages.success(request, 'Login Success')
            return render(request, "authentication/index.html",{"fname":fname})
        else:
            messages.error(request, 'Recheck Credentials.')
            return render(request, "authentication/TeacherLogin.html")

    return render(request, "authentication/TeacherLogin.html")


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser, token):
        myuser.is_active = True
        # user.profile.signup_confirmation = True
        myuser.save()
        login(request, myuser)
        messages.success(request, 'Your Account has been activated')
        return redirect('student_signin')
    else:
        return render(request, 'activation_failed.html')

# Create your views for teachers here


def signout(request):
    logout(request)
    messages.success(request, 'Logged Out Successfully!')
    return redirect('index')

