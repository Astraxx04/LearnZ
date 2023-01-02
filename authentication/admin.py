from django.contrib import admin
from .models import *
# Register your models here.

models = [Student,Teacher]
admin.site.register(models)

