from django.shortcuts import render, redirect
from django.http import FileResponse
from UploadFiles.models import notes,sylabus,quiz
from django.contrib import messages
import sqlite3
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def studentFeatures(request):
    cur_course = request.COOKIES.get('course_name')
    syllabus=sylabus.objects.filter(course_name = cur_course).first()
    context = {"syllabus":syllabus}
    return render(request, "features/featuresStudent.html",context)

@login_required
def teacherFeatures(request):
    if request.user.role == "TEACHER":
        return render(request, "features/featuresTeacher.html")    
    else:
        messages.error(request, 'Login as Teacher to continue')
        return redirect('teacher_signin')


@login_required
def suggestedvideos(request):
    cur_course = request.COOKIES.get('course_name')
    syllabus=sylabus.objects.filter(course_name = cur_course).first()
    context = {"syllabus":syllabus}
    return render(request, "features/suggestedvideos.html", context)  
