from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Userprofile, UserMatches, UserLikes, UserDislikes, UserBlock, UserReport


def index(request):
    return render(request, 'signup.html')


def signup(request):
    """
    register users
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        password1 = request.POST.get('pass1')
        password2 = request.POST.get('pass2')
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return HttpResponseRedirect(reverse('user:index'))
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
                return HttpResponseRedirect(reverse('user:index'))
            else:
                user = User.objects.create_user(username=username, email=email, password=password1, first_name=firstname, last_name=lastname)
                user.save()
                return render(request, 'login.html')
        else:
            messages.error(request, 'Passwords do not match')
            return render(request, 'signup.html')
    else:
        return render(request, 'signup.html')


def login_user(request):
    """
    login users
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass1')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return render(request, 'index.html')
        else:
            messages.error(request, 'Invalid username or password')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')