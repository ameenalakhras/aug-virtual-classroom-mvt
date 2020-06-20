from django.db import models
from django.conf import settings
from base.models import BaseModel


class Notification(BaseModel):
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    read = models.BooleanField(default=False)
    content = models.CharField(max_length=1000)

    read_at = models.DateTimeField(null=True)
    received_at = models.DateTimeField(null=True)

