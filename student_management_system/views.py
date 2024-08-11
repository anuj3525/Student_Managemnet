from ast import Return
import email
from multiprocessing import context
from pickle import NONE
import profile
from django.shortcuts import render,redirect
from app.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from app.models import CustomUser


def BASE(request):
    return render(request,'base.html')

def LOGIN(request):
    return render(request,'login.html')

def dologin(request):
    if request.method == "POST":
        user = EmailBackEnd.authenticate(request,
                                         username=request.POST.get('email'),
                                         password=request.POST.get('password'),)
        if user!=None:
            login(request,user)
            user_type = user.user_type
            if user_type == '1':    
                return redirect('hod_home')
            elif user_type == '2':
                return redirect('staff_home')
            elif user_type == '3':
                return redirect('student_home')
            else:
                messages.error(request,'Email and Password are invalid !')
                return redirect('login')
        else:
                messages.error(request,'Email and Password are invalid !')
                return redirect('login')
        

def doLogout(request):
    logout(request)
    return redirect('login')
    
@login_required(login_url='/')
def PROFILE(request):
    user= CustomUser.objects.get(id = request.user.id)

    context = {
        "user":user,
    }
    return render(request,'profile.html', context)

@login_required(login_url='/')
def PROFILE_UPDATE(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        First_name = request.FILES.get('First_name')
        Last_name = request.FILES.get('Last_name')
        #email = request.FILES.get('email')
        #username = request.FILES.get('username')
        password = request.FILES.get('password')
        print(profile_pic)

        try:
            customuser = CustomUser.objects.get(id = request.user.id)

            customuser.First_name = First_name
            customuser.Last_name = Last_name
            customuser.profile_pic = profile_pic    

            if password!=NONE and password != "":
                customuser.set_password(password)
            customuser.save() 

            if profile_pic!=NONE and profile_pic != "":
                customuser.profile_pic = profile_pic
            customuser.save() 
            messages.success(request,'YOUR PROFILE UPDATED SUCCESSFULLY!')
            redirect('profile')

        except:
            messages.error(request,'Failed to Update your Profile')

    return render(request,'profile.html')
