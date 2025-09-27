from django.db import models
from django.contrib.auth.models import AbstractUser
import hashlib

# AbstractUser has usernaem and password by default

class User(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
