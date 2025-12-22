from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponse
from django.contrib import messages
from credentials.models import Profile
from django.db import transaction

# Create your views here.
def register(request):
    if request.method=="POST":
        first_name=request.POST["f_name"]
        last_name=request.POST["l_name"]
        pro_pic=request.FILES.get("profile_picture")
        mail=request.POST["email"]
        password=request.POST["password"]
        if User.objects.filter(username=mail).exists():
            return HttpResponse("User already exists")
        else:
            try:
                with transaction.atomic():
                    user=User.objects.create_user(username=mail,first_name=first_name,last_name=last_name,email=mail,password=password)
                    user.save()
                    Profile.objects.create(user=user,profile_pic=pro_pic)

                    return redirect("signin")
            except Exception as e:
                messages.error(request,"Can't create new user",format(e))               
    return render(request,"register.html")

def login(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST["password"]
        user=auth.authenticate(request,username=email,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("dashboard")
        else:
            # return HttpResponse("Invalid username or password")
            messages.error(request,"Invalid username or password")
            return redirect("signin")
    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect("signin")
