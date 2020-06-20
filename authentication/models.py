from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

from base.models import BaseModel

from authentication.utils import get_avatar_path


class User(AbstractUser):
    email = models.EmailField(unique=True)
    email_verified = models.BooleanField(default=False)
    email_verification_date = models.DateTimeField(null=True)

    def get_profile(self):
        """return the users profile"""
        pass

    def reset_password(self):
        """reset the password for forgotten passwords"""
        pass

    def change_password(self, old_password, new_password):
        """change the password for the user after log in"""
        pass


class UserProfile(BaseModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=get_avatar_path, null=True)

    def __str__(self):
        return self.user.username

