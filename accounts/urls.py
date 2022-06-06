from django.urls import path
from accounts.views import AddDoctorView, DoctorProfileView, UpdateDoctorView, ChangeDoctorPasswordView, UpdatePatientView

urlpatterns = [
    path("add_doctor/", AddDoctorView.as_view(), name="add_doctor"),
    path('profile/<pk>/', DoctorProfileView.as_view(), name='profile'),
    path('update/<pk>/', UpdateDoctorView.as_view(), name='update'),
    path('profile/update/<pk>/', UpdatePatientView.as_view(), name='update_profile'),
    path('change_password/', ChangeDoctorPasswordView.as_view(), name='change_password'),

] 
