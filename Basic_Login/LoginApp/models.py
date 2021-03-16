from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfileInfo(models.Model):

    #this user will fetch field from User class
    user = models.OneToOneField(User,on_delete = models.CASCADE)

    #additional field

    portfolio_site = models.URLField(blank = True)

    profile_pic = models.ImageField(upload_to = 'profile_pic', blank = True )

    def __str__(self):
        return self.user.username
