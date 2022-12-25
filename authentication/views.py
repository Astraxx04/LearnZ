from django.views.decorators.csrf import csrf_exempt
from . import u
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
django.utils.encoding.force_text = force_str


# Create your views here.
def index(request):
    return render(request, "authentication/index.html")


@csrf_exempt
def student_signup(request):
    if request.method == "POST":
        CollegeName = request.POST['CollegeName']
        username = request.POST['usn']
        fname = request.POST['FName']
        lname = request.POST['LName']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['ConfiPass']

        if User.objects.filter(username=username):
            messages.error(
                request, "USN already exist! Please try some other username.")
            return redirect('index')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('index')

        if len(username) > 20:
            messages.error(request, "Usn must be under 20 charcters!!")
            return redirect('index')

        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('index')

        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('index')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        # myuser.last_name = lname
        # myuser.is_active = False
        #myuser.is_active = False
        myuser.save()
        messages.success(
            request, "Your Account has been created succesfully!!.")

        # # Welcome Email
        # subject = "Welcome to LeanZ- Django Login!!"
        # message = "Hello " + myuser.first_name + "!! \n" + \
        #     "Welcome to LeanZ!! \nThank you for visiting our website\n. We have also sent you a confirmation email, please confirm your email address. \n\nThanking You\nAnubhav Madhav"
        # from_email = settings.EMAIL_HOST_USER
        # to_list = [myuser.email]
        # send_mail(subject, message, from_email,
        #           to_list, fail_silently=True)

        # # Email Address Confirmation Email
        # current_site = get_current_site(request)
        # email_subject = "Confirm your Email @ LeanZ - Django Login!!"
        # message2 = render_to_string('email_confirmation.html', {

        #     'name': myuser.first_name,
        #     'domain': current_site.domain,
        #     'uid': urlsafe_base64_encode(u.force_bytes(myuser.pk)),
        #     'token': generate_token.make_token(myuser)
        # })
        # email = EmailMessage(
        #     email_subject,
        #     message2,
        #     settings.EMAIL_HOST_USER,
        #     [myuser.email],
        # )
        # email.fail_silently = True
        # email.send()

        return redirect('student_signin')

    return render(request, "authentication/StudentSignup.html")


@csrf_exempt
def student_signin(request):
    if request.method == 'POST':
        username = request.POST.get('usn',False)
        pass1 = request.POST.get('pass1','')
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            fname = user.first_name
            messages.success(request, "Logged In Sucessfully!!")
            return render(request, "authentication/index.html",{"fname":fname})
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('index')

    return render(request, "authentication/StudentLogin.html")


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
        messages.success(request, "Your Account has been activated!!")
        return redirect('student_signin')
    else:
        return render(request, 'activation_failed.html')


def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('index')
