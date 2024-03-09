from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import User

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        # Check if the email is already associated with an existing account
        if User.objects.filter(email=email).exists():
            messages.error(request, 'An account with this email address already exists.')
            return redirect('register')

        user = User.objects.create(username=username, password=password, email=email)
        user.save()

        return redirect('login')

    return render(request, 'register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Check if both username and password are provided
        if not username or not password:
            messages.error(request, 'Please provide both username and password.')
            return redirect('login')

        user = authenticate(request, username=username, password=password)

        # Check if authentication failed
        if user is None:
            messages.error(request, 'Invalid username or password. Please try again.')
            return redirect('login')

        login(request, user)
        return redirect('home')

    return render(request, 'login.html')
