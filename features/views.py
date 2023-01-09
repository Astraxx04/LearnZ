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
    return render(request, "features/suggestedvideos.html")  

@login_required
def Notes(request):
    sqliteConnection = sqlite3.connect('db.sqlite3')
    cursor = sqliteConnection.cursor()
    print('DB Init')

    if 'courseStudent' in request.session:
        name = request.session['courseStudent']

        query = f"SELECT crs_id FROM course_course WHERE course='{name}' "
        location = cursor.execute(query)
        cursor.close()

        filepath = r'features\tt.pdf'
        return FileResponse(open(filepath, 'rb'), content_type='application/pdf')
        # filename = employee + ".pdf"
        # filepath = os.path.join(settings.MEDIA_ROOT, "payslips", year, month, filename)

    filepath = r'features\tt.pdf'
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')
    return redirect('feature_page_student')

@login_required
def Quiz(request):
    sqliteConnection = sqlite3.connect('db.sqlite3')
    cursor = sqliteConnection.cursor()
    print('DB Init')

    if 'courseStudent' in request.session:
        name = request.session['courseStudent']

        query = f"SELECT crs_id FROM course_course WHERE course='{name}' "
        location = cursor.execute(query)
        cursor.close()

        filepath = r'features\tt.pdf'
        return FileResponse(open(filepath, 'rb'), content_type='application/pdf')
        # filename = employee + ".pdf"
        # filepath = os.path.join(settings.MEDIA_ROOT, "payslips", year, month, filename)

    filepath = r'features\tt.pdf'
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')
    return redirect('feature_page_student')

@login_required
def Syllabus(request):
    sqliteConnection = sqlite3.connect('db.sqlite3')
    cursor = sqliteConnection.cursor()
    print('DB Init')

    if 'courseStudent' in request.session:
        name = request.session['courseStudent']

        query = f"SELECT crs_id FROM course_course WHERE course='{name}' "
        location = cursor.execute(query)
        cursor.close()

        filepath = r'features\tt.pdf'
        return FileResponse(open(filepath, 'rb'), content_type='application/pdf')
        # filename = employee + ".pdf"
        # filepath = os.path.join(settings.MEDIA_ROOT, "payslips", year, month, filename)

    filepath = r'features\tt.pdf'
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')
    return redirect('feature_page_student')

