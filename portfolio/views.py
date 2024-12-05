from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

# Create your views here.
@never_cache
@login_required(login_url='/authentication/login')
def index(request):
    return render(request, 'portfolio/index.html')