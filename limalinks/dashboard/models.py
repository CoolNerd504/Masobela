from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Person(models.Model):
	email = models.EmailField(unique=True)
    name =models.Charfeild