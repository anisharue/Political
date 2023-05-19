from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        username = request.POST['username']
        password = request.POST['password']
        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            error_msg = 'This username is already taken, please choose a different one'
            return render(request, 'registration/register.html', {'error_msg': error_msg})
        # Create a new user
        user = User.objects.create_user(username=username, password=password, first_name=first_name)
        # Automatically log in the user after registration
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'registration/success_register.html', {'username': username})

    return render(request, 'registration/register.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            return render(request, 'registration/success_login.html', {'username': username})

        else:
            # add an error message for invalid credentials
            error_msg = 'Invalid username or password, please try again'
            return render(request, 'registration/login.html', {'error_msg': error_msg, 'username': username})
    return render(request, 'registration/login.html')
