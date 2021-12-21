from accounts.models import User
from appointments.models import Appointment
from django import forms
from accounts.constants import ROLE, SPECIALITIES
import datetime

class AppointmentForm(forms.ModelForm):
    """ This form for create appointment ."""
    specialities = forms.ChoiceField(choices=SPECIALITIES)
    class Meta:
        model = Appointment
        fields = ('specialities', 'doctor', 'appoint_date', 'description')
        widgets = {
            'appoint_date': forms.DateTimeInput(attrs={'type': 'datetime-local','class':'datetimepicker', 'min':datetime.datetime.today()}),
        }

    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        self.fields['doctor'].queryset = User.objects.filter(role=ROLE[0][0])
        if 'specialities' in self.data:   
            spec = self.data.get('specialities')
            doc = User.objects.filter(role=ROLE[0][0])
            self.fields['doctor'].queryset = doc.filter(specialities=spec)
