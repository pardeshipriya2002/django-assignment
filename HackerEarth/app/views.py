from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import models
import csv

# Create your views here.

def index(request):
    all_users=models.User.objects.all()
    return render(request, 'index.html', {'all_users':all_users})

def add_user(request):
    if request.method == 'POST':
        uname = request.POST.get('name')
        uemail = request.POST.get('email')
        umobile = request.POST.get('mobile')
        models.User.objects.create(name=uname, email=uemail, mobile=umobile)
        return redirect('index')
    return render(request, 'useradd.html')

def add_task(request, uid):
    user = models.User.objects.get(userId=uid)
    if request.method == 'POST':    
        tdetail = request.POST.get('taskdetail')
        ttype = request.POST.get('tasktype')
        models.Task.objects.create(task_Assign=user, taskdetail=tdetail, tasktype=ttype)
        return redirect('index')
    return render(request, 'taskadd.html', {'user':user})

def export_data(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="tasks.csv"'
    writer = csv.writer(response)
    writer.writerow(['User ID', 'Name', 'Mobile','Email','task Detail','Task Type'])        
    users  = models.User.objects.all()
    for user in users:
        for task in user.tasks.all():
            writer.writerow([user.userId,user.name,user.mobile,user.email,task.taskdetail,task.tasktype])
    return response