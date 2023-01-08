from django.contrib import admin
from .models import notes,sylabus,quiz

# Register your models here.

admin.site.register(notes)
admin.site.register(sylabus)
admin.site.register(quiz)
