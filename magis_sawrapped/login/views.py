from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User


def user_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        email = request.POST['email']

        # Check if any input field is blank
        if not username or not password or not confirm_password or not email:
            messages.error(request, 'Please fill in all fields.')
            return render(request, 'register.html')

        # Check if the email is already associated with an existing account
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'An account with this email address already exists.')
            return render(request, 'register.html')

        # Check if passwords match
        elif password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'register.html')

        else:
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save() 
            authenticated_user = authenticate(request, username=username, password=password)
            login(request, authenticated_user)
            return render(request, '../../dashboard/templates/dashboard/view_grades.html') 

    return render(request, 'register.html')

def user_login(request):
    if request.method == 'POST':
        identifier = request.POST.get('identifier')
        password = request.POST['password']

        # Check if both identifier and password are provided
        if not identifier or not password:
            messages.error(request, 'Please provide both username/email and password.')
            return render(request, 'login.html')

        # Check if the identifier is an email address
        if '@' in identifier:
            kwargs = {'email': identifier}
        else:
            kwargs = {'username': identifier}

        user = authenticate(request, **kwargs, password=password)

        # Check if authentication failed
        if user is None:
            messages.error(request, 'No account found for the provided username/email and password.')
            return render(request, 'login.html')

        else:
            login(request, user)
            return render(request, '../../dashboard/templates/dashboard/dashboard.html') 

    return render(request, 'login.html')
