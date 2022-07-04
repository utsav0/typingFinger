from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "index.html")
def login(request):
    return HttpResponse("login PAGE")
def signup(request):
    return HttpResponse("signup PAGE")
def practice(request):
    return HttpResponse("practice PAGE")
