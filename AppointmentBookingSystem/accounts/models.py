from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from .constants import ROLE, GENDER, SPECIALITIES
# Create your models here.


class User(AbstractUser):
    """Abstract User table"""
    contact = PhoneNumberField()
    birthdate = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER, blank=True, null=True)
    role = models.CharField(
        max_length=50, choices=ROLE, null=True, blank=True, default=ROLE[1][1]
    )
    specialities = models.CharField(max_length=20, choices=SPECIALITIES, blank=True, null=True)
    photo = models.ImageField(upload_to='image/', blank=True, null=True)

    def __str__(self):
        return str(self.username)
