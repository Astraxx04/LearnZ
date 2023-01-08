from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.


class notes(models.Model):
    file_name = models.CharField(max_length=50)
    my_file = models.FileField(validators=[FileExtensionValidator(allowed_extensions=['pdf','doc','docx','pptx'])])
    course_name = models.CharField(max_length=100)


class quiz(models.Model):
    quiz_name = models.CharField(max_length=30)
    link = models.URLField(max_length=200)
    date = models.DateField(auto_now_add=True)
    course_name = models.CharField(max_length=100)


class sylabus(models.Model):
    file_name = models.CharField(max_length=50)
    my_file = models.FileField()
    course_name = models.CharField(max_length=100)
