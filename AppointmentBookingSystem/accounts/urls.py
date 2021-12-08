from django.urls import path
from accounts.views import AddDoctorView, DoctorProfileView, UpdateDoctorView

urlpatterns = [
    path("add_doctor/", AddDoctorView.as_view(), name="add_doctor"),
    path('profile/<pk>/', DoctorProfileView.as_view(), name='profile'),
    path('update/<pk>/',UpdateDoctorView.as_view(), name='update'),
] 
