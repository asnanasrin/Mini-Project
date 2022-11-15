from urllib import request
from django.shortcuts import render,redirect
from .models import *
from .forms import *
# from django.core.files.storage import FileSystemStorage
# import os
# import numpy as np
# from PIL import Image 

# Create your views here.

def index(request):
    return render(request,'index.html')

def register(request):
    if request.method=="POST":
        id=request.POST.get('id')
        fname=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        phoneNumber=request.POST.get('phoneNumber')
        adrs=request.POST.get('adrs')
        District=request.POST.get('District')
        regmodel(fname=fname,email=email,password=password,phoneNumber=phoneNumber,adrs=adrs,District=District).save()
        return redirect('login')
    else:
     return render(request,'register.html')

def userreg(request):
    if request.method=="POST":
        id=request.POST.get('id')
        uname=request.POST.get('uname')
        email=request.POST.get('uemail')
        upassword=request.POST.get('upassword')
        phoneNumber=request.POST.get('phoneNumber')
        adrs=request.POST.get('adrs')
        District=request.POST.get('District')
        vid=request.POST.get('vid')
        usermodel(uname=uname,email=email,upassword=upassword,phoneNumber=phoneNumber,adrs=adrs,District=District,vid=vid).save()
        return redirect('userlogin')
    else:
     return render(request,'userreg.html')

def login(request):
    return render(request,'login.html')

def log(request):
    if request.method=="POST":
        id=request.POST.get('id')
        fname=request.POST.get('fname')
        password=request.POST.get('password')

        cr=regmodel.objects.filter(fname=fname,password=password)
        if cr:
            user=regmodel.objects.get(fname=fname,password=password)
            id=user.id
            fname=user.fname
            password=user.password
            request.session['id']=id
            request.session['fname']=fname
            request.session['password']=password
            return redirect('home')
        else:
         return render(request,'login.html')
    # else:
    #     return render(request,'register.html')

def userlogin(request):
    return render(request,'userlogin.html')

def userlog(request):
    if request.method== 'POST':
        id=request.POST.get('id')
        vid=request.POST.get('vid')
        upassword=request.POST.get('upassword')
        request.session['vid']=vid
        cr=usermodel.objects.filter(vid=vid,upassword=upassword)
        if cr:
            user=usermodel.objects.get(vid=vid,upassword=upassword)
            id=user.id
            uname=user.uname
            upassword=user.upassword
            vid=user.vid
            request.session['id']=id
            request.session['uname']=uname
            request.session['upassword']=upassword
            
            return redirect('userhome')
        else:
         return render(request,'userlogin.html')

def case(request):
    if request.method=="POST":
        caseid=request.POST.get('caseid')
        casename=request.POST.get('casename')
        discription=request.POST.get('discription')
        location=request.POST.get('location')
        vehicleno=request.POST.get('vehicleno')
        uname=request.POST.get('uname')
        vehicleownerid=request.POST.get('vehicleownerid')
        amount=request.POST.get('amount')
        date=request.POST.get('date')
        casemodel(caseid=caseid,casename=casename,discription=discription,location=location,vehicleno=vehicleno,uname=uname,vehicleownerid=vehicleownerid,amount=amount,date=date).save()
        return redirect('home')
    else:
     return render(request,'case.html')

def home(request):
    return render(request,'home.html')

def view(request):
    cr=rulemodel.objects.all()
    return render(request,'view.html',{'cr':cr})

def userhome(request):
    return render(request,'userhome.html')

def viewcase(request):
    # vehicleno=request.user
    # request.session['vehicleno']
    #uname=request.user
    vid=request.session['vid']
    cr=casemodel.objects.filter(vehicleno=vid)
    print('vehicle id is ',vid)
    return render(request,'viewcase.html',{'cr':cr})
   
    

def result1(request):
        return render(request,'result.html')

def viewchallan(request):
    vid=request.session['vid']
    cr=casemodel.objects.filter(vehicleno=vid)
    print('vehicle id is ',vid)
    return render(request,'viewchallan.html',{'cr':cr})



