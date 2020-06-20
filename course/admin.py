from django.contrib import admin

from course.models import MediaType, Provider, Media


admin.site.register(MediaType)
admin.site.register(Provider)
admin.site.register(Media)
