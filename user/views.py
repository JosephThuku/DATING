from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Userprofile, UserMatches, UserLikes, UserDislikes, UserBlock, UserReport, UserInterest


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
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1, first_name=firstname, last_name=lastname)
                user.save()
                return redirect('login')
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
            return redirect("/dating/home")
        else:
            messages.error(request, 'Invalid username or password')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

@login_required(login_url='/user/login')
def user_profile(request):
    """
    update the user profile
    """
    if request.method == 'POST':
        bio = request.POST.get('bio')
        cumpus = request.POST.get('campus')
        gender = request.POST.get('gender')
        hobbies = request.POST.get('hobbies')
        interests = request.POST.get('interests')
        introvert = request.POST.get('introvert')
        extrovert = request.POST.get('extrovert')
        profile_pic = request.FILES.get('profile_pic')
        career = request.POST.get('career')
        #get current user
        # Get the current user's ID
# Get the current user's ID as an integer
        user_id = request.user.id

        # Now, you can assign the user variable to the user with the current user's ID
       # user = User.objects.get(id=user_id)
        user = user_id
        user_profile = Userprofile.objects.create(profile_picture=profile_pic, bio=bio, campus=cumpus, gender=gender, user_id=user)
        user_profile.save()

        user_intrest = UserInterest.objects.create(hobbies=hobbies, interest=interests, introvert='False', extrovert='True', career=career, user_id=user)
        user_intrest.save()

        return redirect('/dating/home')
    else:
        return render(request, 'profile.html')


def logout_user(request):
    """
    logout users
    """
    logout(request)
    return redirect('login')

