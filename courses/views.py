from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Courses
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import sqlite3
import json

# Create your views here.
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

@login_required
def course_page(request):
    usn = request.user.username
    courses = getcourses()
    serialized_courses = json.dumps(courses)
    return render(request, "courses/Course_Page.html",{"usn":usn,"courses":serialized_courses})

@login_required
def tcourse(request):
    if request.user.role == "TEACHER":
        username = request.user.username
        courses = getcourses()
        serialized_courses = json.dumps(courses)
        return render(request, "courses/tea_course.html", {"usn":username,"courses":serialized_courses})    
    else:
        messages.error(request, 'Login as Teacher to continue')
        return redirect('teacher_signin')
