from distutils.command.upload import upload
from email.mime import image
from importlib.resources import path
from django.db import models


class Project(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	technology = models.CharField(max_length=20)
	image = models.ImageField(upload_to="../static/projects")
	# image = models.FilePathField(path="../projects")
