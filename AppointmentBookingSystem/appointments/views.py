from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic import ListView, UpdateView
from django.views.generic.detail import DetailView
from accounts.constants import ROLE
from accounts.models import User
from django.db.models import Count
from appointments.forms import AppointmentForm
from appointments.models import STATUS, Appointment
from django.core.mail import send_mail
from AppointmentBookingSystem.settings import EMAIL_HOST_USER


# Create your views here.


class SpecialitiesView(View):
    """for specialities of doctors"""

    def get(self, request):
        doctors = User.objects.filter(role=ROLE[0][0])
        specialities = User.objects.exclude(specialities=None).values('specialities').annotate(Count('specialities'))
        data = {"specialities": specialities, "doctors": doctors}
        return render(request, "specialities.html", data)


class BookAppointment(View):
    """ for create appointment"""

    def get(self, request):
        user = request.GET.get('doctor_id')
        if user:
            spec = User.objects.get(id=user)
            form = AppointmentForm(initial={'specialities': spec.specialities, 'doctor': user})
        else:
            form = AppointmentForm()
        return render(request, 'account/_application_form.html', {'form': form})

    def post(self, request):
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment_data = form.save(commit=False)
            appointment_data.patient = self.request.user
            appointment_data.save()
            subject = "New Appointment..."
            message = "Hello {doctor} \nappointmentt for checkup....\nappointment date :{date} \n description : {desc} ".format(
                doctor=appointment_data.doctor, date=appointment_data.appoint_date,
                desc="http://127.0.0.1:8000/appointments/{p}/".format(p=appointment_data.patient.id))
            send_mail(subject, message, EMAIL_HOST_USER, [appointment_data.doctor.email], fail_silently=False, )
            return redirect('index')
        else:
            form = AppointmentForm()
            return render(request, 'account/_application_form.html', {'form': form})


def load_doc(request):
    spec = request.GET.get('sepc')
    doc = User.objects.filter(specialities=spec)
    return render(request, 'account/_doc_list.html', {'doc_list': doc})


class AppointmentListView(LoginRequiredMixin, ListView):
    """ for appointment list of doctor"""
    model = Appointment
    template_name = "appointment_list.html"
    context_object_name = "appoint_list"

    def get_queryset(self):
        query = Appointment.objects.filter(doctor=self.request.user)
        # for filter and search functionaties
        # filter = self.request.GET.get('filter')
        # search = self.request.GET.get('search', '')

        # if search:
        #     query =  query.filter(patient__username__icontains = search )
        # if filter:
        #     query =  query.filter(status = filter)

        # for datetime gone then save completed
        # for q in query:
        #     if q.appoint_date.date() < datetime.date.today():
        #         q.status = STATUS[2][1]
        #         q.save()
        #     else:
        #         q.status = STATUS[0][0]
        #         q.save()
        return query

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_option'] = Appointment.objects.filter(doctor=self.request.user).values('status').distinct()
        context['filter'] = self.request.GET.get('filter')
        context['search'] = self.request.GET.get('search')
        return context


class AppointmentDetailView(LoginRequiredMixin, DetailView):
    """ detail view of appointment to check"""
    model = Appointment
    template_name = "appointment.html"
    context_object_name = "appointments"


def AppointmentAccept(request, pk, action):
    appointment = Appointment.objects.filter(id=pk)
    if action == "Accept":
        appointment.update(status=STATUS[1][0])
        return redirect('appointment_list')
    # elif action == "Reschedule":
    #     appointment.update(status=STATUS[3][0])
    #     return redirect('appointment_list')
    elif action == "Cancel":
        appointment.update(status=STATUS[4][0])
    appointments = appointment.first()
    return render(request, 'appointment.html', {'appointments': appointments})


class RescheduleView(View):
    def get(self, request, pk):
        appointment = Appointment.objects.filter(id=pk).first()
        print(appointment)
        form = AppointmentForm(instance=appointment)
        form.fields['doctor'].disabled = form.fields['specialities'].disabled = form.fields[
            'specialities'].disabled = True
        print(form)
        return render(request, '_reschedule_form.html', {'form': form})

    def post(self, request, pk):
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment_data = form.save(commit=False)
            appointment_data.save(pk=pk)
            return redirect('index')
        else:
            form = AppointmentForm()
            return render(request, '_reschedule_form.html', {'form': form})
