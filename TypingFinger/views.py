from ctypes.wintypes import PDWORD
from distutils.command import check
from django.http import HttpResponse
from django.shortcuts import render, redirect
from requests import request
from urllib3 import Retry


def home(request):
    return render(request, "index.html")

def signup(request):
    return render(request , "signup.html")

def practice(request):
    return render(request, "practice.html")

def forgotpwd(request):
    return render(request, "forgotpwd.html")

def checkCredentials(email, pwd):
    return True

def login(request):
    email = request.POST.get("email", None)
    pwd = request.POST.get("pwd", None)

    if email != None and pwd != None:
        status = checkCredentials(email, pwd)
        if status == True:
            return redirect("/practice", {1:"one"})
        elif status == False:
            return render(request, "login.html", {"message":"Credentials did not match!"})
    else:
        return render(request, "login.html", {"message":""})

def addNewUser(request):
    email = request.POST.get("email", None)
    pwd = request.POST.get("pwd", None)
    if email != None and pwd != None:
        #add the new user in database
        return render(request, "login.html", {"message":"Signup successful! Please login here:", "msgColor":"green"})
    else:
        return HttpResponse("Ran Into Unknown Error!")
    




