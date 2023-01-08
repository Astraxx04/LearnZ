from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('student', views.studentFeatures, name='feature_page_student'),
    path('teacher', views.teacherFeatures, name='feature_page_teacher'),
    path('question_bank', views.questionBank, name='qbDownload'),
    path('quiz', views.Quiz, name='quizDownload'),
    path('syllabus', views.Syllabus, name='sybDownload'),
    path('suggestedvideos', views.suggestedvideos, name='suggestedvideos'),
]
