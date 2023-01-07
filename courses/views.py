from django.shortcuts import render
from .models import Courses
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def course_page(request):
    usn = User.get_username()
    return render(request, "courses/Course_Page.html", {"usn":usn})

@login_required
def tcourse(request):
    username = User.get_username()
    return render(request, "courses/tea_course.html", {"username":username})