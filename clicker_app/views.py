from django.http import HttpResponse
from django.shortcuts import render, redirect
from clicker_app.forms import UserForm
from django.contrib.auth import authenticate, logout, login
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def index(request):
    response = render(request, 'clicker_app/base.html')
    return response


def about(request):
    response = render(request, 'clicker_app/about.html')
    return response


def tutorial(request):
    response = render(request, 'clicker_app/tutorial.html')
    return response



def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('clicker_app:index'))
            else:
                return HttpResponse("Your account is disabled")
        else:
            print("Invalid login details, please try again")
            return HttpResponse("Invalid login details supplied")
    else:
        response = render(request, 'clicker_app/login.html')
        return response



def signup(request):
    registered = False #registration unsuccessful initially
    if request.method == 'POST': #if form is post, attempt to process
        user_form = UserForm(request.POST) #take information from form
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True #save to databbase, registration successful
        else:
            print(user_form.errors) #invalid attempt
    else:
        user_form = UserForm() #give blank form ready to receive data
    response = render(request, 'clicker_app/signup.html', context={'user_form':user_form,'registered':registered})
    return response



def myaccount(request):
    response = render(request, 'clicker_app/myaccount.html')
    return response

@login_required
def logout_view(request):
    logout(request)
    return redirect(reverse('clicker_app:index'))