from django.db import models
from Admin.models import Movies  
from Admin.models import Premium  


from datetime import timedelta, datetime


# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=25,null=True)
    phone=models.IntegerField(null=True)
    email=models.EmailField()
    password=models.CharField(max_length=50)
    confirm_password=models.CharField(max_length=50)
    



class Complaint(models.Model):
    names=models.CharField(max_length=25,null=True)
    phones=models.IntegerField(null=True)
    emails=models.EmailField()
    messages=models.CharField(max_length=100,null=True)


class contactus(models.Model):
    cname=models.CharField(max_length=25,null=True)
    cemail=models.EmailField()
    cphone=models.IntegerField(null=True)
    categories=models.CharField(max_length=25,null=True)




class Comment(models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE, null=True)  # ✅ Use "Movie" instead of Movies
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # ✅ Track which user commented
    comments = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)  # ✅ Timestamp for when comment is added
    likes = models.IntegerField(default=0)







class MovieReaction(models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    reaction = models.CharField(max_length=10,null=True)  # This is the correct field!





class WatchLater(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE,null=True)
    added_on = models.DateTimeField(auto_now_add=True,null=True)



  
class UserSubscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    subscription = models.ForeignKey(Premium, on_delete=models.SET_NULL, null=True, blank=True)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)
    is_paid = models.BooleanField(default=False)  # ✅ Add this field
