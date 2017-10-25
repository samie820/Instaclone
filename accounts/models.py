from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
# Create your models here.
from django.contrib.auth.models import User, BaseUserManager, AbstractBaseUser, PermissionsMixin


class UserProfile(models.Model):
    
    #models for our user profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    followers = models.ManyToManyField('UserProfile',related_name='followers_profile', blank =True)
    following = models.ManyToManyField('UserProfile', related_name='following_profile', blank=True)
    
    profile_pic= ProcessedImageField(upload_to = 'profile_pics',format = 'JPEG',options = {'quality':100},blank = True,null = True)
    description = models.CharField(max_length=200, null = True, blank=True)


    def get_number_followers(self):
        print(self.followers.count())
        if self.followers.count():
            return self.followers.count()
        else:
            return 0

    def get_number_following(self):
        if self.following.count():
            return self.following.count()
        else:
            return 0

    def __str__(self):
        return self.user.username


