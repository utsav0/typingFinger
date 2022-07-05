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

def checkCredentials(email, pwd):
    # logic to match the credentials
    return True

def practice(request):

    # first verifying weather the user is logined or not
    email = request.POST.get("email", None)
    pwd = request.POST.get("pwd", None)

    if email == None or pwd == None:
        # redirecting to logn first
        return render(request, "login.html", {"message":"Please login first to use the service:", "msgColor":"blue"})

    elif email != None and pwd != None:
        status = checkCredentials(email, pwd)
        if status == True:
            return render(request, "practice.html")
        elif status == False:
            return render(request, "login.html", {"message":"Credentials did not match!"})
        else:
            return HttpResponse("Unknown Error!")

def forgotpwd(request):
    return render(request, "forgotpwd.html")

def login(request):
    return render(request, "login.html", {"message":""})

def addNewUser(request):
    email = request.POST.get("email", None)
    pwd = request.POST.get("pwd", None)
    if email != None and pwd != None:
        #add the new user in database
        return render(request, "login.html", {"message":"Signup successful! Please login here:", "msgColor":"green"})
    else:
        return HttpResponse("Ran Into Unknown Error!")
    
def result(request):
    return HttpResponse("result page")




