from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.


def home(request):

    # check to see if they are logging in
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['password']

        # authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are logged in')
            return redirect('home')
        else:
            messages.success(
                request, 'There was an error logging in. Please try again')
            return redirect('home')

    # if the request is not a post then it's a get so we just show them the home page
    else:
        return render(request, 'home.html', {})


# login


def login_user(request):
    pass


def logout_user(request):
    logout(request)
    messages.success(request, 'You are logged out')
    return redirect('home')
