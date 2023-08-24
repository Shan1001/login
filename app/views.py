from django.shortcuts import redirect, render
from app.models import tbl_login
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse
def login(request):
    return render(request,'login.html')
def form1(request):
    return render(request,'form.html')
def admin1(request):    
    return render(request,'admin1.html')

def user1(request):
    a=request.session['username']
    b=tbl_login.objects.get(username=a)
    c=User.objects.get(username=a)
    return render(request,'user1.html',{'x':a,'y':b,'z':c})
def addlogin(request):
    a=request.POST.get('username')
    b=request.POST.get('password')
    data=authenticate(username=a,password=b)
    request.session['username']=a
    if data is not None and data.is_superuser==1:
        return redirect ('/admin1/')
    elif data is not None and data.is_superuser==0:
        return redirect('/user1/')
    else:
        return HttpResponse('invalid user')

def adduser(request):
    a=tbl_login()
    b=User()
    b.username=request.POST.get('username')
    b.first_name=request.POST.get('firstname')
    b.email=request.POST.get('email')
    b.last_name=request.POST.get('lastname')
    p=request.POST.get('password')
    b.set_password(p)
    a.username=request.POST.get('username')
    a.fisrtname=request.POST.get('firstname')
    a.email=request.POST.get('email')
    a.phone=request.POST.get('phone')
    a.gender=request.POST.get('gender')
    a.age=request.POST.get('age')
    a.address=request.POST.get('address')
    a.save()
    b.save()
    return redirect('/')



# Create your views here.
