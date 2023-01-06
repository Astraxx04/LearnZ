from django.shortcuts import render

# Create your views here.
def studentFeatures(request):
    return render(request, "features/featuresStudent.html")

def teacherFeatures(request):
    return render(request, "features/featuresTeacher.html")    