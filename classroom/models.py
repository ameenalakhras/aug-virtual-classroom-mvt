from django.db import models
from django.conf import settings

from classroom.utils import get_classroom_bg_path, get_classroom_logo_path, get_attachment_path

from base.models import BaseModel


class AttachmentType(BaseModel):
    """
        'classroom' or 'task attachment' for now
    """
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Attachment(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    file = models.FileField(upload_to=get_attachment_path)
    _type = models.ForeignKey(AttachmentType, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class ClassRoom(BaseModel):
    title = models.CharField(max_length=50)
    logo_img = models.ImageField(upload_to=get_classroom_logo_path, null=True)
    background_img = models.ImageField(upload_to=get_classroom_bg_path, null=True)

    description = models.TextField(null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    attachments = models.ManyToManyField(Attachment, blank=True)


class ClassRoomTeacher(BaseModel):
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    user = models.ManyToManyField(settings.AUTH_USER_MODEL)


class Post(BaseModel):
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()


class Comment(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    #defaulted as 0 if it was a comment on a post, if it was a reply on a comment it would take the comment id
    parent_id = models.IntegerField(default=0)
    content = models.TextField()


class Task(BaseModel):
    average_degree = models.IntegerField(null=True)
    # creator: originally a teacher or an assistant
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    attachments = models.ManyToManyField(Attachment, blank=True)


class TaskSolutionInfo(BaseModel):
    attachment = models.ForeignKey(Attachment, on_delete=models.CASCADE)
    notes = models.CharField(max_length=300, null=True)
    accepted = models.BooleanField(null=True)


class TaskSolution(BaseModel):
    accepted = models.BooleanField(null=True)
    solutionInfo = models.ManyToManyField(Attachment, blank=True)
    task = models.OneToOneField(Task, on_delete=models.CASCADE)

