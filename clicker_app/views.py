from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'clicker_app/base.html')

def about(request):
    return HttpResponse("This is the about page")

def tutorial(request):
    return HttpResponse("This is the tutorial page")

def login(request):
    return HttpResponse("This is the login page")

def signup(request):
    return HttpResponse("This is the signup page")

def myaccount(request):
    return HttpResponse("This is the myaccount page")
