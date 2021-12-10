from django.db import models
from django.shortcuts import render
from django.views.generic.base import View
from accounts.constants import ROLE, SPECIALITIES
from accounts.models import User
from django.views.generic import ListView
from django.db.models import Count
from django.contrib.auth.mixins import LoginRequiredMixin
import logging
from django.http import JsonResponse
import copy
# Create your views here.


class SpecialitiesView(View):
    """for specialities of doctors"""
    
    def get(self, request):
        doctors = User.objects.filter(role=ROLE[0][0])
        specialities =  User.objects.exclude(specialities=None).values('specialities').annotate(Count('specialities'))
        print(specialities)
        data = {"specialities": specialities, "doctors":doctors}
        return render(request, "specialities.html", data)
