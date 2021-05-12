from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

class UsernamePasswordService(models.Model):
    service = models.CharField(max_length=30)
    user_name = models.CharField(max_length=15)
    password = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=CASCADE, null=True)

