from django.db import models
from django.forms import ModelForm


# Create your models here.

class Quiz(models.Model):
    crs_id = models.CharField(max_length=20)
    links = models.URLField()

class Syllabus(models.Model):
    crs_id = models.CharField(max_length=20)
    syb_pdf = models.FileField(upload_to='media/')

class QB(models.Model):
    crs_id = models.CharField(max_length=20)
    qb_pdf = models.FileField(upload_to='media/')



