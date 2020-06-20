from django.db import models
from django.conf import settings

from base.models import BaseModel


class InternalEmail(BaseModel):
    """the emails that are sent inside of the website between users (internal messages as emails)"""
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="internal_mail_sender")
    receiver = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="internal_mail_receiver_users")
    title = models.CharField(max_length=50)
    context = models.TextField()
    sent_at = models.DateTimeField(blank=True)
    read = models.BooleanField(default=False)
    read_at = models.DateTimeField(blank=True)


class CompanyOfficialEmail(BaseModel):
    """The company official email addresses that sends emails to users"""
    name = models.CharField(max_length=50)
    email = models.EmailField()


class ExternalEmail(BaseModel):
    """The emails info that get sent to the users"""
    email = models.ForeignKey(CompanyOfficialEmail, on_delete=models.CASCADE, related_name="external_mail_sender")
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="external_mail_sender")
    receiver = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="external_mail_receiver_users")
    title = models.CharField(max_length=50)
    context = models.TextField()
    sent_at = models.DateTimeField(blank=True)
