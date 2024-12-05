from django.shortcuts import render, redirect
from .models import Appointment, Category
from django.contrib import messages
from django.core.paginator import Paginator
import json
from django.http import JsonResponse



# Create your views here.
def search_appointments(request):
    
    if request.method=='POST':
        search_string = json.loads(request.body).get('searchText')
        
        appointments=Appointment.objects.filter(date__startswith=search_string, owner=request.user) | Appointment.objects.filter(description__icontains=search_string, owner=request.user) | Appointment.objects.filter(category__icontains=search_string, owner=request.user)
        
        data=appointments.values()
        
        return JsonResponse(list(data), safe=False)
        
def my_appointments(request):
    # categories=Category.objects.all()
    appointments = Appointment.objects.filter(owner=request.user)
    paginator=Paginator(appointments, 3)
    page_number=request.GET.get('page')
    page_object=Paginator.get_page(paginator, page_number)
    
    context={
        'appointments':appointments,
        'page_obj':page_object
    }
    return render(request, 'appointment/my_appointments.html', context)

def add_appointment(request):
    categories=Category.objects.all()
    context={
        'categories':categories,
        'values':request.POST
    }
    
    if request.method=="GET":
        return render(request, 'appointment/add_appointment.html', context)

    if request.method == "POST":
        description=request.POST['description']
        
        
        if not description:
            messages.error(request, 'Description required')
            return render(request, 'appointment/add_appointment.html', context)
        
        category=request.POST['category']
        date=request.POST['date']
        
        Appointment.objects.create(owner=request.user, description=description, date=date, category=category)
        messages.success(request, 'Appointment created successfully!!')
        return redirect('my_appointments')
    
def edit_appointment(request, id):
    categories=Category.objects.all()
    appointment=Appointment.objects.get(pk=id)
    context={
        'appointment':appointment,
        'values': appointment,
        'categories':categories
        }
    if request.method=="GET":
        
        return render(request, "appointment/edit_appointment.html", context)
    if request.method == "POST":
        description=request.POST['description']
        
        
        if not description:
            messages.error(request, 'Description required')
            return render(request, 'appointment/edit_appointment.html', context)
        
        category=request.POST['category']
        date=request.POST['date']
        
        appointment.owner=request.user
        appointment.description=description
        appointment.date=date
        appointment.category=category
        
        appointment.save()
        
        messages.success(request, 'Appointment Edited successfully!!')
        return redirect('my_appointments')
    
def delete_appointment(request, id):
    appointment=Appointment.objects.get(pk=id)
    appointment.delete()
    messages.success(request, 'Appointment Deleted!!')
    return redirect('my_appointments')
     
    
    