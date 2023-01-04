from django.db import models
# Create your models here.

class Courses(models.Model):
    sem = models.IntegerField()
    crs_id = models.CharField(max_length=20)
    course = models.CharField(max_length=100)
