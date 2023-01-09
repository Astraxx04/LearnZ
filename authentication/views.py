from django.views.decorators.csrf import csrf_exempt
from . tokens import generate_token
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, HttpResponseRedirect
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
import sqlite3
import json

def getcourses():
    sqliteConnection = sqlite3.connect('db.sqlite3')
    cursor = sqliteConnection.cursor()
    sqlite_select_Query = "select * from courses_courses;"
    count_sem1 = "select count(*) from courses_courses where sem = 1;"
    count_sem2 = "select count(*) from courses_courses where sem = 2;"
    count_sem3 = "select count(*) from courses_courses where sem = 3;"
    count_sem4 = "select count(*) from courses_courses where sem = 4;"
    count_sem5 = "select count(*) from courses_courses where sem = 5;"
    count_sem6 = "select count(*) from courses_courses where sem = 6;"
    count_sem7 = "select count(*) from courses_courses where sem = 7;"

    count=[]
    cursor.execute(count_sem1)
    sem1_count = cursor.fetchall()[0][0]
    count.append(sem1_count)

    cursor.execute(count_sem2)
    sem2_count = cursor.fetchall()[0][0]
    count.append(sem2_count)

    cursor.execute(count_sem3)
    sem3_count = cursor.fetchall()[0][0]
    count.append(sem3_count)

    cursor.execute(count_sem4)
    sem4_count = cursor.fetchall()[0][0]
    count.append(sem4_count)

    cursor.execute(count_sem5)
    sem5_count = cursor.fetchall()[0][0]
    count.append(sem5_count)

    cursor.execute(count_sem6)
    sem6_count = cursor.fetchall()[0][0]
    count.append(sem6_count)

    cursor.execute(count_sem7)
    sem7_count = cursor.fetchall()[0][0]
    count.append(sem7_count)


    courses={1:[],2:[],3:[],4:[],5:[],6:[],7:[]}
    sem = 0
    for i in count:
        sem+=1
        row_sem1 = "select course from courses_courses where sem = " + str(sem) +";"
        cursor.execute(row_sem1)
        row = cursor.fetchall()
        courses[sem].append(row)
    #print(sem1_count,sem2_count,sem3_count,sem4_count,sem5_count,sem6_count,sem7_count)
    cursor.close()
    return courses














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
            messages.error(request, 'USN already exists!!')
            return redirect('student_signup')

        if models.Student.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered!!')
            return redirect('student_signup')

        if len(username) > 10:
            messages.error(request, 'USN must be under 10 characters!!')
            return redirect('student_signup')

        if pass1 != pass2:
            messages.error(request, "Passwords didn't match!!")
            return redirect('student_signup')

        if not username.isalnum():
            messages.error(request, 'Username must be Alpha-Numeric!!')
            return redirect('student_signup')

        myuser = models.Student.objects.create_user(username, email, pass1, first_name = fname, last_name = lname)
        #myuser.first_name = fname
        #myuser.last_name = lname
        #myuser.CollegeName = CollegeName
        # myuser.last_name = lname
        # myuser.is_active = False
        #myuser.is_active = False
        myuser.save()
        # pyautogui.alert("Your Account has been created succesfully!!.")
        messages.success(request, 'Signup Successful!!')
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
            messages.error(request, 'TeacherId already exists!!')
            return redirect('teacher_signup')

        if models.Teacher.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered!!')
            return redirect('teacher_signin')

        if len(username) > 10:
            messages.error(request, 'ID must be under 10 characters!!')
            return redirect('teacher_signin')

        if pass1 != pass2:
            messages.error(request, "Passwords didn't match!!")
            return redirect('teacher_signin')

        if not username.isalnum():
            messages.error(request, 'Username must be Alpha-Numeric!!')
            return redirect('teacher_signin')

        myuser = models.Teacher.objects.create_user(username, email, pass1, first_name = fname, last_name = lname)
        #myuser.first_name = fname
        #myuser.last_name = lname
        #myuser.CollegeName = CollegeName
        # myuser.last_name = lname
        # myuser.is_active = False
        #myuser.is_active = False
        myuser.save()
        messages.success(request, 'Signup Successful!!')
        return redirect('teacher_signin')

    return render(request, "authentication/TeacherSignup.html")


def student_signin(request):
    if request.method == 'POST':
        username = request.POST.get('usn',False)
        pass1 = request.POST.get('password','')
        #courses = getcourses()
        user = authenticate(username=username, password=pass1)
        
        if user is not None and user.role == "STUDENT":
            login(request, user)
           # usn = user.get_username()
            messages.success(request, 'Login Successful!!')
           # serialized_courses = json.dumps(courses)
            return redirect("courses/")
        else:
            messages.error(request, 'Invalid USN/Password!!')
            return render(request, "authentication/StudentLogin.html")

    return render(request, "authentication/StudentLogin.html")


def teacher_signin(request):
    if request.method == 'POST':
        username = request.POST.get('teachid',False)
        pass1 = request.POST.get('password','')
        #courses = getcourses()
        user = authenticate(username=username, password=pass1)
        
        if user is not None and user.role == "TEACHER":
            login(request, user)
            messages.success(request, 'Login Successful!!')
            #serialized_courses = json.dumps(courses)
            return redirect("tcourse/")
        else:
            messages.error(request, 'Invalid TeacherID/Password!!')
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

