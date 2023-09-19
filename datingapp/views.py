from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from user.models import Userprofile, UserMatches, UserLikes, UserDislikes, UserBlock, UserReport
# Create your views here.

"""
Views to handle the business logic of dating 
list all available people
enable like and dislike
user messages
"""
@login_required(login_url='/user/login')
def home(request):
    return render(request, 'index.html')


def landing(request):
    return render(request, 'landing.html')