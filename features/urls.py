from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('student', views.studentFeatures, name='feature_page_student'),
    path('teacher', views.teacherFeatures, name='feature_page_teacher'),
]
