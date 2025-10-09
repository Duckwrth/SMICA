from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('client', 'Client'),
        ('psw', 'PSW'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    full_name = models.CharField(max_length=150)

