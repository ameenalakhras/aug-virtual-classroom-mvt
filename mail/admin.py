from django.contrib import admin

from mail.models import ExternalEmail, InternalEmail, CompanyOfficialEmail


admin.site.register(ExternalEmail)
admin.site.register(InternalEmail)
admin.site.register(CompanyOfficialEmail)
