from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models  # Ensure this import is included

class CustomUser(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Make sure this name is unique
        blank=True,
        help_text='The groups this user belongs to.'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',  # Make sure this name is unique
        blank=True,
        help_text='Specific permissions for this user.'
    )
