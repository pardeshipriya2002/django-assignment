from django.contrib import admin
from . import models

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display=('task_Assign', 'taskdetail','tasktype')
    list_filter=('task_Assign','tasktype')

class UserAdmin(admin.ModelAdmin):
    list_display=('userId','name','email','mobile')

admin.site.register(models.User, UserAdmin)
admin.site.register(models.Task, TaskAdmin)