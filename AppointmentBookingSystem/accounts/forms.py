from accounts.models import User
from django import forms
from allauth.account.forms import SignupForm
from phonenumber_field.formfields import PhoneNumberField
from accounts.constants import GENDER, SPECIALITIES


class MyCustomSignupForm(SignupForm):
    """ This form is All auth User registration """
    email = forms.EmailField(
        required=True,
        max_length=122,
        widget=forms.TextInput(
            attrs={"placeholder": "Enter your email name"}
        ),
    )
    username = forms.CharField(
        max_length=122,
        widget=forms.TextInput(
            attrs={"placeholder": "Enter your username"}
        ),
    )
    first_name = forms.CharField(
        max_length=122,
        widget=forms.TextInput(
            attrs={"placeholder": "Enter your first name"}
        ),
    )
    last_name = forms.CharField(
        max_length=122,
        widget=forms.TextInput(
            attrs={"placeholder": "Enter your last name"}
        ),
    )
    contact = PhoneNumberField(
        widget=forms.TextInput(
            attrs={"placeholder": "Enter your contact number"}
        )
    )
    gender = forms.ChoiceField(choices=GENDER)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, request):
        user = super(MyCustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.contact = self.cleaned_data["contact"]
        user.gender = self.cleaned_data["gender"]

        user.save()
        return user

class AddDoctorForm(forms.ModelForm):
    """ This form for create doctor by administration."""
    email = forms.EmailField(
        required=True,
        max_length=122,
        widget=forms.TextInput(
            attrs={"class": "form-control",
                   "placeholder": "Enter your email name"}
        ),
    )
    username = forms.CharField(
        max_length=122,
        widget=forms.TextInput(
            attrs={"class": "form-control",
                   "placeholder": "Enter your username"}
        ),
    )
    first_name = forms.CharField(
        max_length=122,
        widget=forms.TextInput(
            attrs={"class": "form-control",
                   "placeholder": "Enter your first name"}
        ),
    )
    last_name = forms.CharField(
        max_length=122,
        widget=forms.TextInput(
            attrs={"class": "form-control",
                   "placeholder": "Enter your last name"}
        ),
    )
    contact = PhoneNumberField(
        widget=forms.TextInput(
            attrs={"class": "form-control",
                   "placeholder": "Enter your contact number"}
        )
    )
    gender = forms.ChoiceField(choices=GENDER)
    specialities = forms.ChoiceField(choices=SPECIALITIES)
    # photo = forms.ImageField()
    # photo = forms.FileInput()
    
    class Meta:
        model = User
        fields = ('email', 'username', 'first_name',
                  'last_name', 'contact', 'gender', 'specialities', 'photo')
