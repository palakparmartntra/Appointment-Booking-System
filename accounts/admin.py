from django.contrib import admin
from .models import User, Role, Speciality
# Register your models here.
admin.site.register(User)
admin.site.register(Speciality)
admin.site.register(Role)
