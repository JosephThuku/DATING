from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Userprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    bio = models.TextField(max_length=500, blank=True)
    #cumpus to be fk
    campus = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username
    

class UserMatches(models.Model):
    match = models.ForeignKey(User, on_delete=models.CASCADE, related_name='this_usermatches')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='this_userz')
    matchedDate = models.DateTimeField(auto_now_add=True)
    matched = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username + "  matched to" + self.match.username
    

class UserLikes(models.Model):
    like = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    likedDate = models.DateTimeField(auto_now_add=True)
    liked = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username + "  liked" + self.like.username
    

class UserDislikes(models.Model):
    dislike = models.ForeignKey(User, on_delete=models.CASCADE, related_name='disliked_users')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='thisuser')
    dislikedDate = models.DateTimeField(auto_now_add=True)
    disliked = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username + "  disliked" + self.dislike.username
    

class UserBlock(models.Model):
    block = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blocked_users')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='thisuserz')
    blockedDate = models.DateTimeField(auto_now_add=True)
    blocked = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username + "  blocked" + self.block.username

class UserReport(models.Model):
    report = models.ForeignKey(User, on_delete=models.CASCADE, related_name='this_user_report')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='this_userc')
    reportedDate = models.DateTimeField(auto_now_add=True)
    reported = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username + "  reported" + self.report.username
    

class UserLocation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='useruser_location')
    longitude = models.FloatField()
    latitude = models.FloatField()
    locationDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + "  location" + self.longitude + " " + self.latitude
    

class UserInterest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='thisuser_interest')
    hobbies = models.CharField(max_length=100, blank=True)
    interest = models.CharField(max_length=100, blank=True)
    career = models.CharField(max_length=100, blank=True)
    extrovert = models.BooleanField(default=True)
    introvert = models.BooleanField(default=False)


    def __str__(self):
        return self.user.username + "  interest" + self.hobbies + " " + self.interest + " " + self.career


class UserChat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_chat')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipient_chat')
    status = models.BooleanField(default=False)
    message = models.CharField(max_length=100, blank=True)
    chatDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + "  chat" + self.message 
    

class pictures(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_pictures')
    picture = models.ImageField(upload_to='profile_pics/', blank=True)
    pictureDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + "  picture" + self.picture


class UserNotification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_notification')
    notification = models.CharField(max_length=100, blank=True)
    notificationDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + "  notification" + self.notification

