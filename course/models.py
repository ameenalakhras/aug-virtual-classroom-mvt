from django.db import models
from base.models import BaseModel
from django.conf import settings
from classroom.models import ClassRoom


class Provider(BaseModel):
    """ the videos provider (youtube or another source)"""
    name = models.CharField(max_length=50)


class MediaType(BaseModel):
    """
    for example:
        in youtube provider:
            it can be 'playlist' or 'video'
    """
    name = models.CharField(max_length=50)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)


class Media(BaseModel):
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE, related_name="media_classroom")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="media_publisher")
    _type = models.ForeignKey(MediaType, on_delete=models.CASCADE, related_name="media_type")
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, related_name="media_provider")
    path = models.URLField()
