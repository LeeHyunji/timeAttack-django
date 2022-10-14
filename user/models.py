from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    phone = models.CharField(max_length=13, blank=False)
    address = models.CharField(max_length=256, blank=True)