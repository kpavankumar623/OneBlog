from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    phone = models.IntegerField(default = 00000)
    profile_picture = models.ImageField(default='profile_default.jpg' , upload_to = "profile_picture/" )
