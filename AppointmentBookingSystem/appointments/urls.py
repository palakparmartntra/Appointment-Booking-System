from django.urls import path
from .views import SpecialitiesView, BookAppointment
urlpatterns = [
    path('specialities/', SpecialitiesView.as_view(), name="specialities" ),
    path('booking/', BookAppointment.as_view(), name='booking'),
] 
