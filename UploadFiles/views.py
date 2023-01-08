from django.shortcuts import redirect, render
from .forms import MyFileForm
from .models import notes,sylabus
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
def notesbase(request):
    mydata=notes.objects.all()    
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

            exists=notes.objects.filter(my_file=MyFile).exists()

            if exists:
                messages.error(request,'The file %s is already exists...!!!'% MyFile)
            else:
                notes.objects.create(file_name=MyFileName,my_file=MyFile).save()
                messages.success(request,"File uploaded successfully.")
        return redirect("notesbase")

def notesdeleteFile(request,id):
    mydata=notes.objects.get(id=id)    
    mydata.delete()    
    os.remove(mydata.my_file.path)
    messages.success(request,'File deleted successfully.')  
    return redirect('notesbase')

def sylbase(request):
    mydata=sylabus.objects.all()    
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

            exists=sylabus.objects.filter(my_file=MyFile).exists()

            if exists:
                messages.error(request,'The file %s is already exists...!!!'% MyFile)
            else:
                sylabus.objects.create(file_name=MyFileName,my_file=MyFile).save()
                messages.success(request,"File uploaded successfully.")
                suggestfun()
        return redirect("sylbase")

def syldeleteFile(request,id):
    mydata=sylabus.objects.get(id=id)    
    mydata.delete()    
    os.remove(mydata.my_file.path)
    messages.success(request,'File deleted successfully.')  
    return redirect('sylbase')


def suggestfun():

    pdffileobj=open('upload/Testing.pdf','rb')
    pdfreader=PyPDF2.PdfReader(pdffileobj)
    x=len(pdfreader.pages)
    pageobj=pdfreader.pages[0]
    text=pageobj.extract_text()
    print(text)
    r=Rake ()
    r.extract_keywords_from_text(text)
    keyword_extracted = r.get_ranked_phrases()[2:25]
    print(keyword_extracted)
    x=keyword_extracted
    print(x)
    def unwanted_number(x):
        for k in x:
            numbers = re.findall('[0-9]+', k)
            if(numbers):
                x.remove(k)
        print(x)

    def unwanted_text(x):
        for k in x:
            k = re.sub("\d+", "",k)
            text = re.findall('(.*?)dayananda(.*?)', k) or re.findall('(.*?)university(.*?)', k) or re.findall('(.*?)malleshwara(.*?)', k) or re.findall('(.*?)institute(.*?)', k) or re.findall('(.*?)engineering(.*?)', k)
            if(text):
                x.remove(k)
        print(x)


    print(keyword_extracted)
    unwanted_number(x)
    print("\n\n\n")
    unwanted_text(x)


    jsonString = json.dumps(x)
    jsonFile = open("data.json", "w")
    jsonFile.write(jsonString)
    jsonFile.close()