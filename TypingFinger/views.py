from ctypes.wintypes import PDWORD
from distutils.command import check
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from requests import request
from urllib3 import Retry
import os, csv, random

def generateTxt(request, wordCount= 10):

    charList = []

    # getting the csv fiel path
    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, "words.csv")

    with open(file_path, "r") as fh:
        fhReader = list(csv.reader(fh))

        # chosing wordCount number of random words
        wordList = random.choices(list(fhReader[0]), k = wordCount)


        # splitting the words into characters
        for word in wordList:
            charList.append([char for char in word])
        # print(charList)

        # return JsonResponse(["one","two"], safe=False)
        return JsonResponse(charList, safe = False)

def home(request):
    return render(request, "index.html")

def signup(request):
    return render(request , "signup.html")

def checkCredentials(email, pwd):
    # logic to match the credentials
    return True

def practice(request):

            return render(request, "practice.html",{"pythonTxt":generateTxt(request)})

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
    totalWords = request.GET.get("totalWords", None)
    totalChar = request.GET.get("totalChar", None)
    MTWords = request.GET.get("MTWords", None)
    MTChars = request.GET.get("MTChars", None)
    wordAcc = int(100-(int(MTWords)/int(totalWords)))
    charAcc = int(100-(int(MTChars)/int(totalChar)))
    if totalWords == None:
        return redirect("/practice")
    else:
        resultValues = {"totalWords":totalWords, "totalChars":totalChar, "MTWords":MTWords, "MTChars":MTChars, "wordAcc":wordAcc, "charAcc":charAcc}
        return render(request, "result.html", resultValues)




