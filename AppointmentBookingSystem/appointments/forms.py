from accounts.models import User
from appointments.models import Appointment
from django import forms
from accounts.constants import GENDER, ROLE, SPECIALITIES
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.admin import widgets                                       
import datetime

class AppointmentForm(forms.ModelForm):
    """ This form for create appointment ."""

    class Meta:
        model = Appointment
        fields = ('doctor', 'appoint_date', 'description')
        widgets = {
            'appoint_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        self.fields['doctor'].queryset = User.objects.filter(role=ROLE[0][0])

    # def clean(self):
    #     appoint_date = self.cleaned_data['appoint_date']
    #     import code; code.interact(local=dict(globals(), **locals()))

    #     if appoint_date < datetime.datetime.today():
    #         raise forms.ValidationError("The date cannot be in the past!")
    #     return self.cleaned_data
                                                