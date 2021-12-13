from django.db import models
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic import CreateView
from accounts.constants import ROLE, SPECIALITIES
from accounts.models import User
from django.db.models import Count
from appointments.forms import AppointmentForm


# Create your views here.


class SpecialitiesView(View):
    """for specialities of doctors"""
    
    def get(self, request):
        doctors = User.objects.filter(role=ROLE[0][0])
        specialities =  User.objects.exclude(specialities=None).values('specialities').annotate(Count('specialities'))
        data = {"specialities": specialities, "doctors":doctors}
        return render(request, "specialities.html", data)


class BookAppointment(View):
    def get(self, request):
        form = AppointmentForm()
        print(form)
        return render(request, 'account/_application_form.html', {'form': form})    

    def post(self, request):
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment_data = form.save(commit=False)
            appointment_data.patient = self.request.user
            appointment_data.save()
            return redirect('index')
        else:
            form = AppointmentForm()
            return render(request, 'account/_application_form.html', {'form': form}) 