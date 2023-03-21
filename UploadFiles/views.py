from django.shortcuts import redirect, render
from werkzeug.utils import secure_filename
from django.contrib.auth.decorators import login_required
from .forms import MyFileForm,MyQuizForm
from .models import notes,sylabus,quiz
from django.contrib import messages
from django.urls import path
import os
import PyPDF2
import nltk
nltk.download('stopwords')
nltk.download('punkt')
from rake_nltk import Rake
import re
import json

# Create your views here.


lastsyl=""

@login_required
def quizbase(request):
    if request.user.role == "TEACHER":

        cur_course = request.COOKIES.get('course_name')
        mydata=quiz.objects.filter(course_name = cur_course)    
        myform=MyQuizForm()
        if mydata!='':
            context={'form':myform,'mydata':mydata}
            return render(request,'qindex.html',context)
        else:
            context={'form':myform}
            return render(request,"qindex.html",context)
    else:
        messages.error(request, 'Login as Teacher to continue')
        return redirect('teacher_signin')

@login_required
def student_quizbase(request):
    cur_course = request.COOKIES.get('course_name')
    mydata=quiz.objects.filter(course_name = cur_course)
    syllabus=sylabus.objects.filter(course_name = cur_course).first() 
    context={'mydata':mydata,'syllabus':syllabus}
    return render(request,'student_qindex.html',context)
    
@login_required
def quizupload(request):
    if request.user.role == "TEACHER":

        if request.method=="POST":
            myform=MyQuizForm(request.POST,request.FILES)        
            if myform.is_valid():
                quizName = request.POST.get('quiz_name') 
                courseName = request.COOKIES.get('course_name') 
                link = request.POST.get('link')
                quiz.objects.create(quiz_name=quizName,link=link,course_name = courseName).save()
                messages.success(request,"Quiz link uploaded successfully.")
            return redirect("quizbase")
    else:
        messages.error(request, 'Login as Teacher to continue')
        return redirect('teacher_signin')

@login_required
def quizdelete(request,id):
    if request.user.role == "TEACHER":

        mydata=quiz.objects.get(id=id)    
        mydata.delete()    
        #os.remove(mydata.my_file.path)
        messages.success(request,'File deleted successfully.')  
        return redirect('quizbase')  
    else:
        messages.error(request, 'Login as Teacher to continue')
        return redirect('teacher_signin')  

@login_required
def student_notesbase(request):
    cur_course = request.COOKIES.get('course_name')
    mydata=notes.objects.filter(course_name = cur_course)
    syllabus=sylabus.objects.filter(course_name = cur_course).first() 
    context={'mydata':mydata,"syllabus":syllabus}
    return render(request,'student_nindex.html',context)
    

@login_required
def notesbase(request):
    if request.user.role == "TEACHER":

        cur_course = request.COOKIES.get('course_name')
        mydata=notes.objects.filter(course_name = cur_course)    
        myform=MyFileForm()
        if mydata!='':
            context={'form':myform,'mydata':mydata}
            return render(request,'nindex.html',context)
        else:
            context={'form':myform}
            return render(request,"nindex.html",context)
    else:
        messages.error(request, 'Login as Teacher to continue')
        return redirect('teacher_signin')


@login_required
def notesuploadfile(request):
    if request.user.role == "TEACHER":

        if request.method=="POST":
            myform=MyFileForm(request.POST,request.FILES)        
            if myform.is_valid():
                MyFileName = request.POST.get('file_name') 
                MyFile = request.FILES.get('file')
                courseName = request.COOKIES.get('course_name') 
                exists=notes.objects.filter(my_file=MyFile).exists()

                if exists:
                    messages.error(request,'The file %s is already exists...!!!'% MyFile)
                else:
                    notes.objects.create(file_name=MyFileName,my_file=MyFile,course_name=courseName).save()
                    messages.success(request,"File uploaded successfully.")
            return redirect("notesbase")
    else:
        messages.error(request, 'Login as Teacher to continue')
        return redirect('teacher_signin')
        

@login_required
def notesdeleteFile(request,id):
    if request.user.role == "TEACHER":

        mydata=notes.objects.get(id=id)    
        mydata.delete()    
        os.remove(mydata.my_file.path)
        messages.success(request,'File deleted successfully.')  
        return redirect('notesbase')
    else:
        messages.error(request, 'Login as Teacher to continue')
        return redirect('teacher_signin')

@login_required
def sylbase(request):
    if request.user.role == "TEACHER":

        cur_course = request.COOKIES.get('course_name')
        mydata=sylabus.objects.filter(course_name = cur_course)        
        myform=MyFileForm()
        if mydata!='':
            context={'form':myform,'mydata':mydata}
            return render(request,'sindex.html',context)
        else:
            context={'form':myform}
            return render(request,"sindex.html",context)
    else:
        messages.error(request, 'Login as Teacher to continue')
        return redirect('teacher_signin')
    

@login_required
def syluploadfile(request):
    if request.user.role == "TEACHER":

        if request.method=="POST":
            myform=MyFileForm(request.POST,request.FILES)        
            if myform.is_valid():
                MyFileName = request.POST.get('file_name') 
                MyFile = request.FILES.get('file')
                courseName = request.COOKIES.get('course_name')
                exists=sylabus.objects.filter(course_name = courseName).count()

                if exists > 0:
                    messages.error(request,'The syllabus already exists...!!!')
                else:
                    sylabus.objects.create(file_name=MyFileName,my_file=MyFile,course_name=courseName).save()
                    messages.success(request,"File uploaded successfully.")
                lastsyl="upload/"+MyFile.name
                filename = secure_filename(MyFile.filename)
                loc="upload/"+filename
                print(lastsyl)
                suggestfun(loc)
            return redirect("sylbase")
    else:
        messages.error(request, 'Login as Teacher to continue')
        return redirect('teacher_signin')

@login_required
def syldeleteFile(request,id):
    if request.user.role == "TEACHER":

        mydata=sylabus.objects.get(id=id)    
        mydata.delete()    
        os.remove(mydata.my_file.path)
        messages.success(request,'File deleted successfully.')  
        return redirect('sylbase')
    
    else:
        messages.error(request, 'Login as Teacher to continue')
        return redirect('teacher_signin')


def suggestfun(locat):

    pdffileobj=open(locat,'rb')
    pdfreader=PyPDF2.PdfReader(pdffileobj)
    x=len(pdfreader.pages)
    pageobj=pdfreader.pages[0]
    text=pageobj.extract_text()
    r=Rake ()
    r.extract_keywords_from_text(text)
    keyword_extracted = r.get_ranked_phrases()[2:25]
    x=keyword_extracted
    def unwanted_number(x):
        for k in x:
            numbers = re.findall('[0-9]+', k)
            if(numbers):
                x.remove(k)
        

    def unwanted_text(x):
        for k in x:
            k = re.sub("\d+", "",k)
            text = re.findall('(.*?)dayananda(.*?)', k) or re.findall('(.*?)university(.*?)', k) or re.findall('(.*?)malleshwara(.*?)', k) or re.findall('(.*?)institute(.*?)', k) or re.findall('(.*?)engineering(.*?)', k) or re.findall('(.*?)iso(.*?)', k)
            if(text):
                x.remove(k)
        


    unwanted_number(x)
    unwanted_text(x)
    print("\n\n\n")
    print(x)


    jsonString = json.dumps(x)
    jsonFile = open("./features/static/features/json/data.json", "w")
    jsonFile.write(jsonString)
    jsonFile.close()