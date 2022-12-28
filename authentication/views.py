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
        username = request.POST['teachid']
        fname = request.POST['FName']
        lname = request.POST['LName']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['ConfiPass']

        if User.objects.filter(username=username):
            # pyautogui.alert("USN already exist! Please try some other username.")
            return redirect('teacher_signup')

        if User.objects.filter(email=email).exists():
            # pyautogui.alert("Email Already Registered!!")
            return redirect('teacher_signup')

        if len(username) > 20:
            # pyautogui.alert("Usn must be under 20 charcters!!")
            return redirect('teacher_signup')

        if pass1 != pass2:
            # pyautogui.alert("Passwords didn't matched!!")
            return redirect('teacher_signup')

        if not username.isalnum():
            # pyautogui.alert("Username must be Alpha-Numeric!!")
            return redirect('teacher_signup')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        # myuser.last_name = lname
        # myuser.is_active = False
        #myuser.is_active = False
        myuser.save()
        # pyautogui.alert("Your Account has been created succesfully!!.")


        return redirect('student_signin')

    return render(request, "authentication/StudentSignup.html")

def teacher_signup(request):
    #baba
    if request.method == "POST":
        CollegeName = request.POST['CollegeName']
        username = request.POST['teacherid']
        fname = request.POST['FName']
        lname = request.POST['LName']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['ConfiPass']

        if User.objects.filter(username=username):
            # pyautogui.alert("teacherid already exist! Please try some other username.")
            return redirect('index')

        if User.objects.filter(email=email).exists():
            # pyautogui.alert("Email Already Registered!!")
            return redirect('index')

        if len(username) > 20:
            # pyautogui.alert("Usn must be under 20 charcters!!")
            return redirect('index')

        if pass1 != pass2:
            # pyautogui.alert("Passwords didn't matched!!")
            return redirect('index')

        if not username.isalnum():
            # pyautogui.alert("Username must be Alpha-Numeric!!")
            return redirect('index')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        # myuser.last_name = lname
        # myuser.is_active = False
        #myuser.is_active = False
        myuser.save()
        # pyautogui.alert("Your Account has been created succesfully!!.")


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
            # pyautogui.alert("Logged In Sucessfully!!")
            return render(request, "courses/Course_Page.html",{"fname":fname})
        else:
            return redirect('index')

    return render(request, "authentication/StudentLogin.html")

def teacher_signin(request):
    if request.method == 'POST':
        username = request.POST.get('teacherid',False)
        pass1 = request.POST.get('pass1','')
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "authentication/index.html",{"fname":fname})
        else:
            return redirect('index')

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
        # pyautogui.alert("Your Account has been activated!!")
        return redirect('student_signin')
    else:
        return render(request, 'activation_failed.html')


def signout(request):
    logout(request)
    # pyautogui.alert("Logged Out Successfully!!")
    return redirect('index')



# Create your views for teachers here

def teacher_signup(request):
    if request.method == "POST":
        CollegeName = request.POST['CollegeName']
        username = request.POST['usn']
        fname = request.POST['FName']
        lname = request.POST['LName']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['ConfiPass']

        if User.objects.filter(username=username):
            # pyautogui.alert("USN already exist! Please try some other username.")
            return redirect('student_signup')

        if User.objects.filter(email=email).exists():
            # pyautogui.alert("Email Already Registered!!")
            return redirect('student_signup')

        if len(username) > 20:
            # pyautogui.alert("Usn must be under 20 charcters!!")
            return redirect('student_signup')

        if pass1 != pass2:
            # pyautogui.alert("Passwords didn't matched!!")
            return redirect('student_signup')

        if not username.isalnum():
            # pyautogui.alert("Username must be Alpha-Numeric!!")
            return redirect('student_signup')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        # myuser.last_name = lname
        # myuser.is_active = False
        #myuser.is_active = False
        myuser.save()
        # pyautogui.alert("Your Account has been created succesfully!!.")


        return redirect('student_signin')

    return render(request, "authentication/StudentSignup.html")

def teacher_signup(request):
    #baba
    if request.method == "POST":
        CollegeName = request.POST['CollegeName']
        username = request.POST['teacherid']
        fname = request.POST['FName']
        lname = request.POST['LName']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['ConfiPass']

        if User.objects.filter(username=username):
            # pyautogui.alert("teacherid already exist! Please try some other username.")
            return redirect('index')

        if User.objects.filter(email=email).exists():
            # pyautogui.alert("Email Already Registered!!")
            return redirect('index')

        if len(username) > 20:
            # pyautogui.alert("Usn must be under 20 charcters!!")
            return redirect('index')

        if pass1 != pass2:
            # pyautogui.alert("Passwords didn't matched!!")
            return redirect('index')

        if not username.isalnum():
            # pyautogui.alert("Username must be Alpha-Numeric!!")
            return redirect('index')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        # myuser.last_name = lname
        # myuser.is_active = False
        #myuser.is_active = False
        myuser.save()
        # pyautogui.alert("Your Account has been created succesfully!!.")


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
            # pyautogui.alert("Logged In Sucessfully!!")
            return render(request, "courses/Course_Page.html",{"fname":fname})
        else:
            return redirect('index')

    return render(request, "authentication/StudentLogin.html")

def teacher_signin(request):
    if request.method == 'POST':
        username = request.POST.get('teacherid',False)
        pass1 = request.POST.get('pass1','')
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "authentication/index.html",{"fname":fname})
        else:
            return redirect('index')

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
        # pyautogui.alert("Your Account has been activated!!")
        return redirect('student_signin')
    else:
        return render(request, 'activation_failed.html')


def signout(request):
    logout(request)
    # pyautogui.alert("Logged Out Successfully!!")
    return redirect('index')

