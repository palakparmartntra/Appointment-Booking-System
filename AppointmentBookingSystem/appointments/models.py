from django.db import models
from accounts.models import User
from django.urls import reverse
from appointments.constants import STATUS

# Create your models here.


class Appointment(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patient')
    doctor = models.ForeignKey(User, on_delete=models.CASCADE,  related_name='doctor')
    appoint_date = models.DateTimeField(null=True, blank=True)
    update_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS, null=True, blank=True, default=STATUS[0][0])
    description = models.TextField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('appointment', kwargs={'pk': self.id})
