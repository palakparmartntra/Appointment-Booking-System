from django.db import models
from django.shortcuts import render
from django.views.generic.base import View
from accounts.constants import ROLE, SPECIALITIES
from accounts.models import User
from django.db.models import Count

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
        return render(request, 'specialities.html')