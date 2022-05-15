from django.urls import path
from .views import SpecialitiesView, BookAppointment, AppointmentListView, AppointmentDetailView, RescheduleView
from . import views
urlpatterns = [
    path('specialities/', SpecialitiesView.as_view(), name="specialities" ),
    path('booking/', BookAppointment.as_view(), name="booking"),
    path('appointment_list/', AppointmentListView.as_view(), name="appointment_list"),
    path('load_doc/', views.load_doc, name="load_doc" ),
    path('<pk>/', AppointmentDetailView.as_view(), name="appointment"),
    path('accept/<int:pk>/', views.appointment_accept, name="appointment_cancel"),
    path('accept/<int:pk>/<str:action>/', views.appointment_accept, name="appointment_cancel"),
    path('reschedule/<pk>', RescheduleView.as_view(), name="reschedule"),
] 
