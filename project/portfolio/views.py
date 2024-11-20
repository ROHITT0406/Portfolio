from django.shortcuts import render,redirect
from portfolio.models import Contact,Blog,Internship
from django.contrib import messages
from datetime import datetime
# Create your views here.
def homee(request):
    return render(request,"home2.html")
def home(request):
    return render(request,"home.html")
def about(request):
    return render(request,"about.html")
def internship(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login First")
        redirect("/auth/login/")
    if request.method=="POST":
        name=request.POST.get("name")
        usn=request.POST.get("usn")
        email=request.POST.get("email")
        offer=request.POST.get("offerletter")
        col_name=request.POST.get("cname")
        sdate=request.POST.get("sdate")
        edate=request.POST.get("edate")
        project=request.POST.get("project")
        
        name=name.upper()
        usn=usn.upper()
        col_name=col_name.upper()
        check1=Internship.objects.filter(usn=usn)
        check2=Internship.objects.filter(email=email)
        if check1 or check2:
            messages.warning(request,"Your details is already submitted")
            return redirect('/internship')
        
        user=Internship(fullname=name,usn=usn,email=email,college_name=col_name,offer_status=offer,start_date=sdate,end_date=edate,proj_report=project)
        user.save()
        return redirect("intern.html")
    return render(request,"intern.html")
def contact(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        phoneno=request.POST.get("phoneNo")
        desc=request.POST.get("desc")
        contact=Contact(name=name,email=email,phoneNo=phoneno,desc=desc)
        contact.save()
        messages.success(request,"Response is sent")
        return redirect("/contact")
    return render(request,"contact.html")
def blogs(request):
    post=Blog.objects.all()
    context={"posts":post}
    return render(request,"blog.html",context)