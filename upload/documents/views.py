        
from django.shortcuts import render,HttpResponse,redirect

from . models import myuploadfile

# Create your views here.
def index(request):
    context = {
        "data":myuploadfile.objects.all(),
    }
    return render(request,"index.html",context)

def send_files(request):
    if request.method == "POST" :
        name = request.POST.get("filename")
        myfile = request.FILES.getlist("uploadfoles")
        
        for f in myfile:
            myuploadfile(f_name=name,myfiles=f).save()
        
        return redirect("fileapp:index")


        