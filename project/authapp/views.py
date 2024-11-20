from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def signup(request):
    if request.method=="POST":
        get_email=request.POST.get("email")
        get_username=request.POST.get("username")
        get_password=request.POST.get("pass1")
        get_confirm_password=request.POST.get("pass2")
        if get_password != get_confirm_password:
            messages.info(request,"password is not match")
            return redirect("/auth/signup/")
        try:
            if User.objects.get(username=get_username):
                messages.warning(request,"UserName is taken")
                return redirect('/auth/signup/')
        except Exception as identifier:
            pass
        myuser=User.objects.create_user(get_username,get_email,get_password)
        myuser.save()
        myuser= authenticate(username=get_username,password=get_password)
        if myuser is not None:
            login(request,myuser)
            return redirect('home')
        messages.success(request,"user is created please Login")
        return redirect('/auth/login/')
    return render(request,"signup.html")
def handleLogin(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("pass1")
        user= authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.success(request,"Invalid Credentials")
    return render(request,"login.html")
def handleLogout(request):
    logout(request)
    messages.success(request,"logout successfully")
    return render(request,"login.html")