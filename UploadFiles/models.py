from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.


class notes(models.Model):
    file_name = models.CharField(max_length=50)
    my_file = models.FileField(validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

class sylabus(models.Model):
    file_name = models.CharField(max_length=50)
    my_file = models.FileField(validators=[FileExtensionValidator(allowed_extensions=['pdf'])])