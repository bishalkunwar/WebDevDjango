from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class mails(models.Model):
    name=models.CharField(max_length=70)
    email=models.EmailField(max_length=100)
    c_number=models.IntegerField()
    message=models.TextField(max_length=2000)