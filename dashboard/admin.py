from django.contrib import admin
from dashboard.models import Task, Supervisor
from actstream.models import Action

admin.site.register(Task)
admin.site.register(Supervisor)

# admin.site.register(Action)