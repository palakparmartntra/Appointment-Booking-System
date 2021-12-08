from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from accounts.models import User
from accounts.forms import AddDoctorForm
from accounts.constants import ROLE
import logging


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
                # import code; code.interact(local=dict(globals(), **locals()))
                userdata = form.save(commit=False)
                userdata.photo = request.POST.get('photo')
                print(userdata)
                userdata.role = ROLE[0][0]
                userdata.set_password(userdata.email)
                userdata.email_verified = True
                userdata.save()
                return redirect('index')
            return render(request, 'account/add_doctor.html', {'form': form})
        except Exception as e:
            logging.error(str(e))
            return render(request, 'account/add_doctor.html', {'form': form})
 