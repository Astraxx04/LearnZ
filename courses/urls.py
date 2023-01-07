from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('courses/', views.course_page, name='course_page'),
    path('tcourse/', views.tcourse, name='tcourse'),
]
