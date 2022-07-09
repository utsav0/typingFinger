import mysql.connector as mycon
from ctypes.wintypes import PDWORD
from distutils.command import check
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from requests import request
from urllib3 import Retry
import os
import csv
import random
from decouple import config  # for the secret key
dbUser = config("dbUser")
dbPassword = config("dbPassword")
dbName = config("dbName")

# this generate random text:
def generateTxt(request, wordCount=10):
    charList = []

    # getting the csv fiel path
    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, "words.csv")

    with open(file_path, "r") as fh:
        fhReader = list(csv.reader(fh))

        # chosing wordCount number of random words
        wordList = random.choices(list(fhReader[0]), k=wordCount)

        # splitting the words into characters
        for word in wordList:
            charList.append([char for char in word])
        return JsonResponse(charList, safe=False)


def home(request):
    return render(request, "index.html")


def signup(request):
    return render(request, "signup.html")


def isMatched(email, pwd):
    con = mycon.connect(host="localhost",
                        database=dbName,
                        user=dbUser,
                        password=dbPassword)
    cur = con.cursor()
    cur.execute(
        f'select * from usertable where mail = "{email}" and password = "{pwd}";')
    return len(cur.fetchall())


def practice(request, status="not valid"):
    email = request.POST.get("email", None)
    pwd = request.POST.get("pwd", None)

    # when credential matches or is redirected from result page:
    if isMatched(email, pwd) or status == "valid":
        return render(request, "practice.html", {"pythonTxt": generateTxt(request)})

    # when credentials are wrong:
    elif email != None and pwd != None:
        return render(request, "login.html", {"message": "Credentials did not matched:", "msgColor": "red"})

    # when someone directly enter the url:
    else:
        return redirect("/login")


def forgotpwd(request):
    return render(request, "forgotpwd.html")


def login(request):
    return render(request, "login.html", {"message": ""})


def userAlreadyExist(cur, email):
    cur.execute(f"select mail from usertable where mail in ('{email}');")
    return(len(cur.fetchall()))


def addNewUser(request):
    pwd = request.POST.get("pwd", None)
    email = request.POST.get("email", None)
    if email != None and pwd != None:
        con = mycon.connect(host="localhost",
                            database=dbName,
                            user=dbUser,
                            password=dbPassword)
        cur = con.cursor()
        if userAlreadyExist(cur, email):
            return render(request, "signup.html", {"message": "This email is already registered with us!"})
        else:
            cur.execute(
                f"""insert into usertable values("{email}", "{pwd}"); """)
            con.commit()
            return render(request, "login.html", {"message": "Signup successful! Please login here:", "msgColor": "green"})
    else:
        return HttpResponse("Ran Into Unknown Error!")


def result(request):
    totalWords = request.GET.get("totalWords", None)
    totalChar = request.GET.get("totalChar", None)
    MTWords = request.GET.get("MTWords", None)
    MTChars = request.GET.get("MTChars", None)
    if totalWords == None:
        return redirect("/login")
    else:
        wordAcc = int(100-(int(MTWords)/int(totalWords)))
        charAcc = int(100-(int(MTChars)/int(totalChar)))
        resultValues = {"totalWords": totalWords, "totalChars": totalChar,
                        "MTWords": MTWords, "MTChars": MTChars, "wordAcc": wordAcc, "charAcc": charAcc}
        return render(request, "result.html", resultValues)


def gotopractice(request):
    btnResponse = request.POST.get("resultBtnStatus", None)
    if btnResponse == "from result":
        return practice(request, "valid")
    else:
        return HttpResponse("Error Occured!")
