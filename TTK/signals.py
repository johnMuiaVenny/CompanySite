from .models import *
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save


@receiver(post_save, sender=User)
def Creat_Profile(sender, instance, created, **kwargs):
    if created:
        PROFILE.objects.create(user=instance, Image='Profile/4.jpg', FName=instance.first_name, LName=instance.last_name, Email=instance.email)



@receiver(post_save, sender=User)
def Update_Profile(sender, instance, created, **kwargs):
    if created == False:
        instance.profile.save()
