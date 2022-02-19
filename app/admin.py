from django.contrib import admin
from .models import WorkOutRecord, WorkOutDetailRecord, WorkOutMenu

admin.site.register(WorkOutRecord)
admin.site.register(WorkOutDetailRecord)
admin.site.register(WorkOutMenu)