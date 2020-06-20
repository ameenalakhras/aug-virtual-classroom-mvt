from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    """
    a Base Model to load the create_date and modified_date
    fields into all the tables in the DataBase
    """
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True


class SoftDeleteModel(BaseModel):
    deleted_at = models.DateTimeField(null=True)
    deleted = models.BooleanField(default=False)

    def delete(self):
        self.deleted = True
        self.deleted_at = timezone.now()
        super().save()

    # telling django that the SoftDeleteModel is an abstract class
    class Meta:
        abstract = True
