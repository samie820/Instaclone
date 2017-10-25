from datetime import datetime
from django.db import models
from django.contrib.auth.models import User, BaseUserManager, AbstractBaseUser, PermissionsMixin
from accounts.models import UserProfile
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

from datetime import datetime


class IGPost(models.Model):
    user_profile = models.ForeignKey(UserProfile, null=True, blank=True)
    title = models.CharField(max_length=100)
    image = ProcessedImageField(upload_to='posts',
                                #processors=[ResizeToFill(200,200)],
                                format='JPEG',
                                options={ 'quality': 100})
    posted_on = models.DateTimeField(auto_now_add=True)

    def get_number_of_likes(self):
        return self.like_set.count()

    def get_number_of_comments(self):
        return self.comment_set.count()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('IGPost')
    user = models.ForeignKey(User)
    comment = models.CharField(max_length=100)
    posted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment


class Like(models.Model):
    post = models.ForeignKey('IGPost')
    user = models.ForeignKey(User)

    class Meta:
        unique_together = ("post", "user")

    def __str__(self):
        return 'Like: ' + self.user.username + ' ' + self.post.title


class Room(models.Model):
    label = models.SlugField(unique=True)
    receiver = models.ForeignKey(User, related_name="receiver")
    sender = models.ForeignKey(User, related_name="sender")

    def get_last_message(self):
        message = Message.objects.filter(room=self).last()
        return message.text if message else ""

    def get_last_message_timestamp(self):
        message = Message.objects.filter(room=self).last()
        return message.timestamp if message else ""

    def __str__(self):
        return self.label


class Message(models.Model):
    room = models.ForeignKey(Room, related_name="messages")
    sender = models.ForeignKey(User)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return self.text + " S:" + self.sender.username
