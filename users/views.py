from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.models import User

def custom_login(request):
    if request.method == 'POST':
        # Assuming 'username' and 'password' are the input names in your HTML form
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            # Redirect to home or any desired page upon successful login
            return redirect('home')

    return render(request, 'users/login.html')


def custom_register(request):
    if request.method == 'POST':
        # Assuming 'username', 'email', 'password', and 'confirm_password' are input names in your HTML form
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('con_password')

        # Check if the user with the given username or email already exists
        if User.objects.filter(username=username).exists() :
            # Handle the case where the user already exists
            # You might want to show an error message or redirect to a different page
            return redirect('home')  # Replace with the desired behavior for existing users

        # Check if passwords match
        if password != confirm_password:
            # Handle the case where passwords do not match
            # You might want to show an error message or redirect to a different page
            return redirect('home')  # Replace with the desired behavior for password mismatch

        # Create a new user
        user = User.objects.create_user(username=username, email=email, password=password)

        # Authenticate and login the new user
        login(request, user)

        # Redirect to home or any desired page upon successful registration
        return redirect('login_page')

    return render(request, 'users/login.html')  # Change this to the correct template for registration


def home(request):
  return render(request , 'users/home.html')

