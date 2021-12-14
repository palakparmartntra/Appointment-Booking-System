from django.urls import path
from .views import SpecialitiesView, BookAppointment, AppointmentListView
urlpatterns = [
    path('specialities/', SpecialitiesView.as_view(), name="specialities" ),
    path('booking/', BookAppointment.as_view(), name="booking"),
    path('appointment_list/', AppointmentListView.as_view(), name="appointment_list"),
] 
