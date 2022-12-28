from django.shortcuts import render

# Create your views here.


def course_page(request):
    return render(request, "Course_Page.html")