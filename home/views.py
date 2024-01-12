from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login ,logout

# Create your views here.
def home(request):
  return render(request,'home/home.html')

def about(request):
  return render(request,'home/about.html')

def contact(request):
  return render(request,'home/contact.html')

#def shore(request):
 # return render(request,'home/shore.html')

def dologout(request):
    logout(request)
    return redirect('login')
