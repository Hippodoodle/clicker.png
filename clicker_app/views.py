from django.http import HttpResponse

def index(request):
    return HttpResponse("This is the index page")

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
