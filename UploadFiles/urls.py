from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('notesuploadfile',views.notesuploadfile,name="notesuploadfile"),
    path('notesbase',views.notesbase,name="notesbase"),
    path('notesdeleteFile/<int:id>',views.notesdeleteFile),
    path('syluploadfile',views.syluploadfile,name="syluploadfile"),
    path('sylbase',views.sylbase,name="sylbase"),
    path('syldeleteFile/<int:id>',views.syldeleteFile),
]
