from django.db import models
from django.contrib.auth.models import User

# Dashboard.models
class Task(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(null=True, blank = True)
	def __str__(self):
		return self.name


class Supervisor(models.Model):
	user = models.ForeignKey(User, null=True, related_name="supervisor")
	task = models.ManyToManyField(Task, related_name="task")
	def __str__(self):
		return self.user.name
