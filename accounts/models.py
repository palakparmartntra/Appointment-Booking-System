from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls.base import reverse
from phonenumber_field.modelfields import PhoneNumberField
from .constants import ROLE, GENDER, SPECIALITIES

class Role(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return str(self.name)


class Speciality(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)


class User(AbstractUser):
    """Abstract User table"""
    contact = PhoneNumberField()
    birthdate = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER, blank=True, null=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True, blank=True)
    specialities = models.ForeignKey(Speciality, on_delete=models.CASCADE, blank=True, null=True)
    photo = models.ImageField(upload_to='image/', blank=True, null=True)
    email_verified = models.BooleanField(default=False)

    def __str__(self):
        return str(self.username)

    def get_absolute_url(self):
        return reverse('profile', kwargs={'pk': self.id })
