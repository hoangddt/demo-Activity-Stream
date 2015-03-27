from django.contrib import admin
from dashboard.models import Task, Supervisor
# from actstream import action

admin.site.register(Task)
admin.site.register(Supervisor)

# admin.site.register(action)