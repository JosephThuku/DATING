from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('login', views.login_user, name='login'),
    path('profile', views.user_profile, name='profile'),
]
