from accounts.models import User, Speciality
from appointments.models import Appointment
from django import forms
from accounts.constants import ROLE, SPECIALITIES
import datetime


class AppointmentForm(forms.ModelForm):
    """ This form for create appointment ."""
    specialities = forms.ModelChoiceField(queryset=Speciality.objects.all(),
                                    to_field_name = 'name',
                                    empty_label="Select Speciality")

    class Meta:
        model = Appointment
        fields = ('specialities', 'doctor', 'appoint_date', 'description')
        widgets = {
            'appoint_date': forms.DateTimeInput(
                attrs={'type': 'datetime-local', 'class': 'datetimepicker', 'min': 'datetime.datetime.today()'}),
        }

    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        self.fields['doctor'].queryset = User.objects.filter(role__name=ROLE[0][0])
        if 'specialities' in self.data:
            breakpoint()
            spec = self.data.get('specialities')
            speciality = Speciality.objects.get(name=spec)
            doc = User.objects.filter(role__name=ROLE[0][0])
            self.fields['doctor'].queryset = doc.filter(specialities=speciality)


class RescheduleForm(forms.ModelForm):
    """ This form for reschedule appointment by doctor."""
    class Meta:
        model = Appointment
        fields = ('appoint_date', 'description')
        widgets = {
            'appoint_date': forms.DateTimeInput(
                attrs={'type': 'datetime-local', 'class': 'datetimepicker', 'min': 'datetime.datetime.today()'}),
        }
