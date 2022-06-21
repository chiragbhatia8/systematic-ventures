from django.db import models

from django.contrib.auth.models import AbstractBaseUser, Permission


class Role(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    permissions = models.ManyToManyField(Permission, blank=True)

    def __str__(self):
        return self.name

class User(AbstractBaseUser):
    USERNAME_FIELD = 'username'

    username = models.CharField(max_length=50, unique=True)
    role = models.ManyToManyField(Role, blank=True)
    email = models.EmailField(blank=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.email


