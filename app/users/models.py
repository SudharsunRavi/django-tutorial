from django.db import models

class User(models.Model):
    username = models.CharField(max_length=20, unique=True)
    bio = models.TextField(blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
