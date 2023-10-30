from django.shortcuts import render
from .models import *
from django.http import   HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages


from django.urls import reverse
def front(request):
        return render(request,"front.html")


def signup(request):
        if request.method=="GET":
                return render(request,"signup.html")
        if request.method =="POST":
                username=request.POST.get('username')
                email=request.POST.get('email')
                age=request.POST.get('age')
                phone=request.POST.get('phone')
                location=request.POST.get('location')
                aadhar=request.POST.get('aadhar')
                password=request.POST.get('password')
                obj1=user(username=username,email=email,age=age,phone=phone,location=location,aadhar=aadhar,password=password)
                obj1.save()
                messages.success(request,"Your accout created")
                return  redirect("/login")

def login(request):
        if request.method=='GET':
                return render(request,"login.html")
        elif request.method == 'POST':
               email=request.POST.get('email')
               password=request.POST.get('password')
               creds=user.objects.filter(email=email,password=password)
               if creds:
                       messages.success(request,"You are logged in")
                       return redirect("/home")
               else:
                       messages.error(request,'Invalid Credentials')
                       return HttpResponse("USER NOT FOUND")
               

def home(request):
        if request.method=="GET":
                return render(request,"home.html")


def register(request):
        if request.method=="GET":
                return render(request,"signup.html")
        if request.method =="POST":
                gstin=request.POST.get('gstin')
                companyname=request.POST.get('companyname')
                location=request.POST.get('location')
                contact=request.POST.get('contact')
                password=request.POST.get('password')
                obj2=company(gstin=gstin,companyname=companyname,location=location,contact=contact,password=password)
                obj2.save()
                messages.success(request,"Company registered successfully")
                return redirect("/login")

def clogin(request):
        if request.method=='GET':
                return render(request,"login.html")
        if request.method == 'POST':
                gstin=request.POST.get('gstin')
                password=request.POST.get('password')
                creds=company.objects.filter(gstin=gstin,password=password)
                if creds:
                        messages.success(request,"You logged in")
                        return redirect('/employeelogin')
                else:
                       messages.error(request,'Invalid Credentials')
                       return HttpResponse("USER NOT FOUND")
               
def employeelogin(request):
        if request.method=="GET":
                return render(request,"employeelogin.html")
        
def alogin(request):
        if request.method=='GET':
                return render(request,"login.html")
        if request.method == 'POST':
               adminname=request.POST.get('adminname')
               adminpass=request.POST.get('adminpass')
               creds=administrator.objects.filter(adminname='adminitjobster@gmail.com',adminpass='Admin@itjobster')
               if creds:
                       messages.success(request,"You are logged in")
                       return redirect("/home")
               else:
                       messages.error(request,'Invalid Credentials')
                       return HttpResponse("USER NOT FOUND")