from django.shortcuts import redirect, render
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

def quizbase(request):
    cur_course = request.COOKIES.get('course_name')
    mydata=quiz.objects.filter(course_name = cur_course)    
    myform=MyQuizForm()
    if mydata!='':
        context={'form':myform,'mydata':mydata}
        return render(request,'qindex.html',context)
    else:
        context={'form':myform}
        return render(request,"qindex.html",context)

def student_quizbase(request):
    cur_course = request.COOKIES.get('course_name')
    mydata=quiz.objects.filter(course_name = cur_course) 
    context={'mydata':mydata}
    return render(request,'student_qindex.html',context)
    

def quizupload(request):
    if request.method=="POST":
        myform=MyQuizForm(request.POST,request.FILES)        
        if myform.is_valid():
            quizName = request.POST.get('quiz_name') 
            courseName = request.COOKIES.get('course_name') 
            link = request.POST.get('link')
            quiz.objects.create(quiz_name=quizName,link=link,course_name = courseName).save()
            messages.success(request,"Quiz link uploaded successfully.")
        return redirect("quizbase")

def quizdelete(request,id):
    mydata=quiz.objects.get(id=id)    
    mydata.delete()    
    #os.remove(mydata.my_file.path)
    messages.success(request,'File deleted successfully.')  
    return redirect('quizbase')    

def student_notesbase(request):
    cur_course = request.COOKIES.get('course_name')
    mydata=notes.objects.filter(course_name = cur_course)
    context={'mydata':mydata}
    return render(request,'student_nindex.html',context)
    



def notesbase(request):
    cur_course = request.COOKIES.get('course_name')
    mydata=notes.objects.filter(course_name = cur_course)    
    myform=MyFileForm()
    if mydata!='':
        context={'form':myform,'mydata':mydata}
        return render(request,'nindex.html',context)
    else:
        context={'form':myform}
        return render(request,"nindex.html",context)

def notesuploadfile(request):
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

def notesdeleteFile(request,id):
    mydata=notes.objects.get(id=id)    
    mydata.delete()    
    os.remove(mydata.my_file.path)
    messages.success(request,'File deleted successfully.')  
    return redirect('notesbase')

def sylbase(request):
    cur_course = request.COOKIES.get('course_name')
    mydata=sylabus.objects.filter(course_name = cur_course)        
    myform=MyFileForm()
    if mydata!='':
        context={'form':myform,'mydata':mydata}
        return render(request,'sindex.html',context)
    else:
        context={'form':myform}
        return render(request,"sindex.html",context)

def syluploadfile(request):
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
            loc="upload/"+MyFile.name
            print(lastsyl)
            suggestfun(loc)
        return redirect("sylbase")

def syldeleteFile(request,id):
    mydata=sylabus.objects.get(id=id)    
    mydata.delete()    
    os.remove(mydata.my_file.path)
    messages.success(request,'File deleted successfully.')  
    return redirect('sylbase')


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