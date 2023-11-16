from django.contrib import admin
from django.urls import path,include
from .views import *  
from . import views
urlpatterns = [
    path("",views.front,name="front"),
    path("signup",views.signup,name="signup"),
    path("login",views.login,name="login"),
    path("home",views.home,name="home"),
    path("register",views.register,name="register"),
    path("clogin",views.clogin,name="clogin"),
    path("alogin",views.alogin,name="alogin"),
    path("resume",views.resume,name="resume"),
    path("postjobs",views.postjobs,name="postjobs"),
    path("coprofile",views.coprofile,name="cprofile"),
    path("myresume",views.myresume,name="myresume")
]
