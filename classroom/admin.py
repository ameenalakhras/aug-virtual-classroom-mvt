from django.contrib import admin

from classroom.models import AttachmentType, Attachment, ClassRoom,\
                             ClassRoomTeacher, Comment, Task, TaskSolutionInfo,\
                             TaskSolution


admin.site.register(AttachmentType)
admin.site.register(Attachment)
admin.site.register(ClassRoom)
admin.site.register(ClassRoomTeacher)
admin.site.register(Comment)
admin.site.register(Task)
admin.site.register(TaskSolutionInfo)
admin.site.register(TaskSolution)
