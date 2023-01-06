from django.urls import path
from . import views


app_name = "fileapp"

urlpatterns = [
    
    path("",views.index),
    path("upload",views.send_files,name="uploads")

]