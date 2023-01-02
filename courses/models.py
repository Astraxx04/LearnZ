from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import PermissionsMixin

class Courses(models.Model):
    semester = models.IntegerField(primary_key=True)
    course1 = models.CharField(max_length=100, blank=True)
    course2 = models.CharField(max_length=100, blank=True)
    course3 = models.CharField(max_length=100, blank=True)
    course4 = models.CharField(max_length=100, blank=True)
    course5 = models.CharField(max_length=100, blank=True)
    course6 = models.CharField(max_length=100, blank=True)
