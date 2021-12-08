from django.urls import path, include

from accounts.views import AddDoctorView

urlpatterns = [
    path("add_doctor/", AddDoctorView.as_view(), name="add_doctor"),
] 
