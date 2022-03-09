import logging

from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic import CreateView, UpdateView
from accounts.models import User
from accounts.forms import AddDoctorForm, ChangePasswordForm, UpdateDoctorForm, UpdatePatientForm
from accounts.constants import ROLE
import logging
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib import messages
from accounts.tasks import send_invitation_email

# Create your views here.

class AddDoctorView(LoginRequiredMixin, CreateView):
    """for add doctor signup by admin"""
    model = User
    form_class = AddDoctorForm
    template_name = 'account/add_doctor.html'
    success_url = 'index'

    def post(self, request, *args, **kwargs):
        try:
            form = AddDoctorForm(request.POST, request.FILES)
            if form.is_valid():
                userdata = form.save(commit=False)
                userdata.role = ROLE[0][0]
                userdata.set_password(userdata.email)
                userdata.email_verified = True
                userdata.is_staff = True
                userdata.save()
                print(userdata)
                # Account.set_email(self, userdata)
                send_invitation_email.delay(self, userdata)
                messages.success(request, 'add doctor successfully!')
                return redirect('index')
            return render(request, 'account/add_doctor.html', {'form': form})
        except Exception as e:
            logging.error(str(e))
            return render(request, 'account/add_doctor.html', {'form': form})


class DoctorProfileView(LoginRequiredMixin, DetailView):
    """Doctor's detailed profile view"""
    model = User
    template_name = 'account/profile.html'
    context_object_name = "profile"


class UpdateDoctorView(LoginRequiredMixin, UpdateView):
    """User or admin can update the profile of user"""
    model = User
    form_class = UpdateDoctorForm
    template_name = 'account/update_profile.html'


class UpdatePatientView(LoginRequiredMixin, UpdateView):
    """User or admin can update the profile of user"""
    model = User
    form_class = UpdatePatientForm
    template_name = 'account/update_profile.html'


class ChangeDoctorPasswordView(PasswordChangeView):
    """for doctor to change their password"""
    model = User
    form_class = ChangePasswordForm
    template_name = 'account/change_password.html'
    success_url = reverse_lazy('index')
