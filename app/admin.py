from django.contrib import admin
from .models import WorkOutRecord, WorkOutRepsRecord, WorkOutMenu

admin.site.register(WorkOutRecord)
admin.site.register(WorkOutRepsRecord)
admin.site.register(WorkOutMenu)