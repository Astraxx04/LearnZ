from django.shortcuts import render

# Create your views here.
def student_log(request):
    return render(request, 'login/student_login.html')

