from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
   path('my_appointments', views.my_appointments, name='my_appointments'),
   path('add_appointment', views.add_appointment, name='add_appointment'),
   path('edit_appointment/<int:id>', views.edit_appointment, name='edit_appointment'),
   path('delete_appointment/<int:id>', views.delete_appointment, name='delete_appointment'),
   path('search_appointments', csrf_exempt(views.search_appointments), name='search_appointments'),
   path('appointment_dash', views.appointment_dash, name='appointment_dash'),
]