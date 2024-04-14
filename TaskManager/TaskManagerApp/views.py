from django.shortcuts import render,HttpResponse
from .models import *
# Create your views here.
def home(request):
    UserData = User.objects.all()
    TaskData = Task.objects.all()
    alldata = {
       'data' : UserData,
       'task' : TaskData,
    }
    return render(request,"index.html",alldata)

def registration(request):
    print(request.method)
    print(request.POST)
    print(request)
    if request.method == 'POST':
        name = request.POST['name']
        print(name)
        email = request.POST.get('email')
        print(email)
        mobile = request.POST.get('mobile')
        print(mobile)
        data1 = User.objects.create(Name=name,Email=email,Mobile=mobile)
        return render(request,"registration.html")
    return render(request,"registration.html")
    
# def submitdata(request):
   
#     return HttpResponse('data recieved' + name)