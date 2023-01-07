from django.db import models

# Create your models here.


class notes(models.Model):
    file_name = models.CharField(max_length=50)
    my_file = models.FileField()

class sylabus(models.Model):
    file_name = models.CharField(max_length=50)
    my_file = models.FileField()