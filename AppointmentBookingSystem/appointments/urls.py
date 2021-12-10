from django.urls import path
from .views import SpecialitiesView
urlpatterns = [
    path('specialities/', SpecialitiesView.as_view(), name="specialities" ),
] 
