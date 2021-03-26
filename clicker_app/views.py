from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    response = render(request, 'clicker_app/base.html')
    return response


def about(request):
    response = render(request, 'clicker_app/about.html')
    return response


def tutorial(request):
    response = render(request, 'clicker_app/tutorial.html')
    return response



def login(request):
    response = render(request, 'clicker_app/login.html')
    return response



def signup(request):
    response = render(request, 'clicker_app/signup.html')
    return response



def myaccount(request):
    response = render(request, 'clicker_app/myaccount.html')
    return response
