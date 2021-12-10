from appointments.models import Appointment
from django import forms
from accounts.constants import GENDER, SPECIALITIES
from django.contrib.auth.forms import PasswordChangeForm


class AppointmentForm(forms.ModelForm):
    """ This form for create appointment ."""
    
    class Meta:
        model = Appointment
        fields = ('doctor', 'appoint_date', 'description')
