from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    phone = models.IntegerField(default = 00000)
    profile_picture = models.ImageField(default='profile_default.jpg' , upload_to = "profile_picture/" )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        image = Image.open(self.profile_picture.path)

        if image.height > 300 or image.width > 300:
            size = (300,300)
            image.thumbnail(size)
            image.save(self.profile_picture.path)
