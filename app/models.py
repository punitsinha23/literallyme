from django.db import models

# Create your models here.
class detail(models.Model):
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)