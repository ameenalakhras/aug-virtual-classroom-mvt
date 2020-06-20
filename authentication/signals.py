from authentication.models import UserProfile
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile(sender, instance, **kwargs):
    """signal handler to create a user profile after the account is created."""
    if kwargs["created"]:
        UserProfile.objects.create(user=instance)
