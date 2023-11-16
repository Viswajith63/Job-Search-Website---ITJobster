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
                        return render(request,"cprofile.html",{
                                "cid":creds[0].cid
                        })
                else:
                       messages.error(request,'Invalid Credentials')
                       return HttpResponse("USER NOT FOUND")
               

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
               
def resume(request):
        if request.method=="GET":
                return render(request,"resume.html")
        if request.method=="POST":
                
                name=request.POST.get('name')
                job_title=request.POST.get('job-title')
                email=request.POST.get('email')
                phone=request.POST.get('phone')
                website=request.POST.get('website')
                linkedin=request.POST.get('linkedin')
                degree=request.POST.get('degree')
                university=request.POST.get('university')
                graduationyear=request.POST.get('graduation-year')
                skills=request.POST.get('skills')
                spokenlanguages=request.POSt.get('spoken-languages')
                job=request.POSt.get('job')
                company=request.pOSt.get('company')
                employmentdates=request.POST.get('employment-dates')
                jobdescription=request.POST.get('job-description')
                personaldescription=request.POST.get('personal-description')
                obj3=Resume(name=name,job_title=job_title,email=email,phone=phone,website=website,linkedin=linkedin,degree=degree,university=university,
                            graduation_year=graduationyear,skills=skills,spoken_languages=spokenlanguages,job_experience=job,personal_description=personaldescription)
                obj3.save()
                messages.success(request,"Resume registered successfully")
                return redirect("/resume")
        

def postjobs(request):
        if request.method=="GET":
                return render(request,"postjob.html")
        if request.method=="POST":
                
                jtitle=request.POST.get('title')
                jlocation=request.POST.get('location')
                jtype=request.POST.get('jobtype')
                skills=request.POST.get('skills')
                exp=request.POST.get('experience')
                vacancy=request.POST.get('vacancies')
                pj=postjob(jtitle=jtitle,jlocation=jlocation,jtype=jtype,jskills=skills,jexperience=exp,jvacancies=vacancy)
                pj.save()
                messages.success(request,"Job Posted Successfully!")
                return redirect("/postjobs")





def coprofile(request):
        if request.method=="GET":
                return render(request,"cprofile.html")
        if request.method == "POST":
                cname=request.POST.get('name')
                cwebsite=request.POST.get('website')
                clocations=request.POST.get('locations')
                jpname=request.POST.get('jpname')
                jpdes=request.POST.get('jpdes')
                jpemail=request.POST.get('email')
                jpphone=request.POST.get('phone')
                jdes=request.POST.get('cdes')
                cp=cprofile(cname=cname,cwebsite=cwebsite,clocations=clocations,jpostername=jpname,jposterdesignation=jpdes,jposteremail=jpemail,jposterphone=jpphone,description=jdes)
                cp.save()
                messages.success(request,"Company profile created successfully")
                return redirect('/postjobs')