from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic import CreateView, ListView
from accounts.constants import ROLE, SPECIALITIES
from accounts.models import User
from django.db.models import Count
from appointments.forms import AppointmentForm
from appointments.models import STATUS, Appointment
from django.http import JsonResponse
# Create your views here.


class SpecialitiesView(View):
    """for specialities of doctors"""
    
    def get(self, request):
        doctors = User.objects.filter(role=ROLE[0][0])
        specialities =  User.objects.exclude(specialities=None).values('specialities').annotate(Count('specialities'))
        data = {"specialities": specialities, "doctors":doctors}
        return render(request, "specialities.html", data)


class BookAppointment(View):
    """ for create appointment"""
    def get(self, request): 
        user = request.GET.get('doctor_id')
        if user:
            spec = User.objects.get(id = user)
            form = AppointmentForm(initial={'specialities':spec.specialities ,'doctor': user})

            print(spec.specialities)
            print(user)
        else:
            form = AppointmentForm()
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

def load_doc(request):
    spec = request.GET.get('sepc')
    doc = User.objects.filter(specialities = spec)
    return render(request, 'account/_doc_list.html', {'doc_list': doc }) 

class AppointmentListView(LoginRequiredMixin, ListView):
    """ for appointment list of doctor"""
    model = Appointment
    template_name = "appointment_list.html"
    context_object_name = "appoint_list"
    

    def get_queryset(self):
        filter = self.request.GET.get('filter')
        search = self.request.GET.get('search', '')
        query = Appointment.objects.filter(doctor=self.request.user)
        print(search)
        print(filter)
        if search:
            query =  query.filter(patient__username__icontains = search )
        if filter:
            query =  query.filter(status = filter) 
        return query 
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_option'] = Appointment.objects.filter(doctor = self.request.user).values('status').distinct()
        context['filter'] = self.request.GET.get('filter')
        context['search'] = self.request.GET.get('search')
        return context

