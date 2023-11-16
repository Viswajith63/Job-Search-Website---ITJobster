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
                obj=postjob.objects.all()
                return render(request,"home.html",{
                        "data":obj,
                })
        
        if request.method=="POST":
                jid=request.POST.get('job-id')
                email=request.POST.get('email')
                ak=applicant(jid=postjob.objects.get(pk=jid),resume=Resume.objects.get(pk=email))
                ak.save()
                return HttpResponse(status=204)


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
                        print(creds[0].cid)
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
                       return redirect("/admin1")
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
                spokenlanguages=request.POST.get('spoken-languages')
                job=request.POST.get('job')
                personaldescription=request.POST.get('personal-description')
                obj3=Resume(name=name,job_title=job_title,email=email,phone=phone,website=website,linkedin=linkedin,degree=degree,university=university,
                            graduation_year=graduationyear,skills=skills,spoken_languages=spokenlanguages,job_experience=job,personal_description=personaldescription)
                obj3.save()
                messages.success(request,"Resume registered successfully")
                return HttpResponse(status=204) 
        
def postjobs(request):
        if request.method=="GET":
                return render(request,"postjob.html")
        if request.method=="POST":
                cid=request.POST.get('cid')
                jtitle=request.POST.get('title')
                jlocation=request.POST.get('location')
                jtype=request.POST.get('jobtype')
                skills=request.POST.get('skills')
                exp=request.POST.get('experience')
                vacancy=request.POST.get('vacancies')
                pj=postjob(cid=cid,jtitle=jtitle,jlocation=jlocation,jtype=jtype,jskills=skills,jexperience=exp,jvacancies=vacancy)
                pj.save()
                messages.success(request,"Job Posted Successfully!")
                return redirect("/postjob")



def coprofile(request):
        if request.method=="GET":
                return render(request,"cprofile.html")
        if request.method == "POST":
                cid=request.POST.get('cid')
                print(cid)
                cname=request.POST.get('name')
                cwebsite=request.POST.get('website')
                clocations=request.POST.get('locations')
                jpname=request.POST.get('jpname')
                jpdes=request.POST.get('jpdes')
                jpemail=request.POST.get('email')
                jpphone=request.POST.get('phone')
                jdes=request.POST.get('cdes')
                cp=cprofile(cid=cid,cname=cname,cwebsite=cwebsite,clocations=clocations,jpostername=jpname,jposterdesignation=jpdes,jposteremail=jpemail,jposterphone=jpphone,description=jdes)
                cp.save()
                messages.success(request,"Company profile created successfully")
                return render(request,"postjob.html",{
                        "data":cid
                })
        
def myresume(request):
        if request.method=="GET":
                return render(request,"myresume.html",{
                        "boo":False,
                })
        if request.method=="POST":
                email=request.POST.get('email')
                obj=Resume.objects.get(pk=email)
                return render(request,"myresume.html",{
                        "boo":True,
                        "data":obj,
                })
        
def checkresume(request,cid=-1):
        if request.method=="GET":
                o1=postjob.objects.filter(cid=cid)
                lis=[]
                for i in o1:
                        lis.append(i.jid)
                o2=applicant.objects.filter(jid__in=lis)
                li2=[]
                for i in o2.values():
                        li2.append(Resume.objects.get(pk=i['resume_id']))
                return render(request,"application.html",{
                        "data":o2,
                        "data1":li2
                })
        if request.method=="POST":
                email=request.POST.get('email')
                obj=Resume.objects.get(pk=email)
                print(cid)
                return render(request,"displayresume.html",{
                        "data":obj,
                        "data1":cid,
                })
        
def goto(request,cid=-1):
        if request.method=="GET":
                return render(request,"postjob.html",{
                        "data":cid,
                })
        
def admin1(request):
    users = user.objects.all()
    companie=company.objects.all()
    return render(request, 'admin.html', {'users': users,"companies":companie})