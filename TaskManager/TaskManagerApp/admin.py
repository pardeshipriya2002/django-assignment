from django.contrib import admin
from .models import *
# Register your models here.

class Student(admin.ModelAdmin):
    list_display=['Name']
admin.site.register(User,Student)
admin.site.register(Task)