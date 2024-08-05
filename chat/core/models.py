from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class Message(models.Model):
    message = models.CharField(max_length=550)
    title = models.CharField(max_length=50, default="Yanıt Başlığı")

    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages', null=True)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages', null=False)
    replyStatus = models.BooleanField(default=False)
    createdAt = models.DateTimeField(default=datetime.now, blank=True)
    deletedAt = models.DateTimeField(null=True, blank=True)
    readStatus = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.sender} --> {self.receiver} : {self.title} / {self.message}"
"""     
    dmId = models.BigIntegerField()

    
    sendStatus = models.BooleanField(default=False)

 

class Contacts(models.Model):
    userId1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contacts_1')
    userId2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contacts_2')"""

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

