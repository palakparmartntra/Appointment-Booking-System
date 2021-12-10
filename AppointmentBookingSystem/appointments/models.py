from django.db import models
from accounts.models import User
# Create your models here.
STATUS=(
    ('Upcoming', 'Upcoming'),
    ('Completed', 'Completed'),
    ('Rescheduled', 'Rescheduled'),
    ('Cancelled', 'Cancelled'),
)

class Appointment(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patient')
    doctor = models.ForeignKey(User, on_delete=models.CASCADE,  related_name='doctor')
    appoint_date = models.DateTimeField()
    update_date = models.DateTimeField()
    status = models.CharField(max_length=50, choices=STATUS, null=True, blank=True)
    description = models.TextField()

