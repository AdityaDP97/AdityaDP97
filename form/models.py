from django.db import models

# Create your models here.
class form(models.Model):
	name=models.CharField(max_length=255)
	last_name=models.CharField(max_length=255)
	email=models.CharField(max_length=255)
	subject=models.CharField(max_length=255)
	msg=models.TextField(max_length=255)