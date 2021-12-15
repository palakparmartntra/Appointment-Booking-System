from accounts.models import User
from appointments.models import Appointment
from django import forms
from accounts.constants import ROLE
import datetime

class AppointmentForm(forms.ModelForm):
    """ This form for create appointment ."""

    class Meta:
        model = Appointment
        fields = ('doctor', 'appoint_date', 'description')
        widgets = {
            'appoint_date': forms.DateTimeInput(attrs={'type': 'datetime-local','class':'datetimepicker', 'min':datetime.datetime.today()}),
        }


    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        self.fields['doctor'].queryset = User.objects.filter(role=ROLE[0][0])
