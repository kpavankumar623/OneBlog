from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UserProfile
import logging

logger = logging.getLogger(__name__)
@receiver(post_save, sender = User)
def create_userprofile(sender, instance, created, **kwargs):
    if created:
        logger.debug("user created sucesfully")
        UserProfile.objects.create(user = instance)
    else:
        logger.error("creation fail")

@receiver(post_save, sender = User)
def save_userprofile(sender,instance,**kwargs):
    instance.userprofile.save()
