from django.contrib import admin
from .models import Appointment, Category

# Register your models here.
admin.site.register(Appointment)
admin.site.register(Category)