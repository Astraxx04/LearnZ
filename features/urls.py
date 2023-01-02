from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.feature_page, name='feature_page'),
]
