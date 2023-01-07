from django.shortcuts import redirect, render
from .forms import MyFileForm
from .models import notes,sylabus
from django.contrib import messages
from django.urls import path
import os

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
        return redirect("sylbase")

def syldeleteFile(request,id):
    mydata=sylabus.objects.get(id=id)    
    mydata.delete()    
    os.remove(mydata.my_file.path)
    messages.success(request,'File deleted successfully.')  
    return redirect('sylbase')