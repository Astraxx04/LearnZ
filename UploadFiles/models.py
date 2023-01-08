from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.


class notes(models.Model):
    file_name = models.CharField(max_length=50)
    my_file = models.FileField(validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

class quiz(models.Model):
    quiz_name = models.CharField(max_length=30)
    link = models.URLField(max_length=200)
    date = models.DateField(auto_now_add=True)

class sylabus(models.Model):
    file_name = models.CharField(max_length=50)
    my_file = models.FileField(validators=[FileExtensionValidator(allowed_extensions=['pdf'])])