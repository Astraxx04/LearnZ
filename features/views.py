from django.shortcuts import render, redirect
from django.http import FileResponse
from UploadFiles.models import notes,sylabus,quiz
import sys
import sqlite3

# Create your views here.
def studentFeatures(request):
    cur_course = request.COOKIES.get('course_name')
    syllabus=sylabus.objects.filter(course_name = cur_course).first()
    context = {"syllabus":syllabus}
    return render(request, "features/featuresStudent.html",context)

def teacherFeatures(request):
    return render(request, "features/featuresTeacher.html")    

def suggestedvideos(request):
    return render(request, "features/suggestedvideos.html")  

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

