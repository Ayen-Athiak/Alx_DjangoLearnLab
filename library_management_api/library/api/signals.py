# api/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser, LibraryUser




# Signal to create a LibraryUser profile whenever a new CustomUser is created
@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        LibraryUser.objects.create(user=instance)

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    instance.libraryuser.save()
