from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.contrib import messages
from django.core.mail import EmailMessage
from django.core.mail.backends.smtp import EmailBackend
from django.core.mail import send_mail
from django.conf import settings

from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site

from django.urls import reverse
from django.contrib import auth
from django.contrib.auth import logout


from .utils import token_generator

import json

# Create your views here.
class HomeView(View):
    def get(self, request):
        return render(request,'authentication/home.html')
    
class LogoutView(View):
    def post(self, request):
        logout(request)
        messages.success(request, 'Logged-Out')
        return redirect('login')
    
class EmailValidationView(View):
    def post(self, request):
        data=json.loads(request.body)
        email = data['email']
        if not validate_email(email):
            return JsonResponse({'email_error': 'Invalid Email'}, status=400)
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error': 'email taken'}, status=409)
        return JsonResponse({'email_valid': 'True'})
    
class UsernameValidationView(View):
    def post(self, request):
        data=json.loads(request.body)
        username = data['username'] 
        if not str(username).isalnum():
            return JsonResponse({'username_error': 'Only alphaNumeric allowed'}, status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error': 'username taken'}, status=409)
        return JsonResponse({'username_valid': 'True'})

class LoginView(View):
    def get(self, request):
        return render(request, 'authentication/login.html')
    
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        
        if username and password:
            user = auth.authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    auth.login(request, user)
                    messages.success(request, 'Successfully logged in!!')
                    return redirect('portfolio')
                messages.error(request, 'Account is not active, please check your email')
                return render(request, 'authentication/login.html')
            messages.error(request, 'Invalid credentials, try again!')
            return render(request, 'authentication/login.html')
        messages.error(request, 'Please fill all fields')
        return render(request, 'authentication/login.html')
    
    
class RegisterView(View):
    def get(self, request):
        return render(request, 'authentication/register.html')
    def post(self, request):
       username = request.POST['username']
       user_email = request.POST['email']
       password = request.POST['password']
       
       context = {
           "fieldValues": request.POST
       }
       
       if not User.objects.filter(username=username).exists():
           if not User.objects.filter(email=user_email).exists():
               if len(password) < 6:
                   messages.error(request, 'Password too short, should be at least 6 characters')
                   return render(request, 'authentication/register.html', context)
               user = User.objects.create_user(username=username, email=user_email)
               user.set_password(password)
               user.is_active=False
               user.save()
               
               uidb64 = urlsafe_base64_encode(force_bytes(force_str(user.pk)))
               token = token_generator.make_token(user)
               domain= get_current_site(request).domain
               link = reverse('activate', kwargs={'uidb64': uidb64, 'token': token})
               activate_url = "http://"+domain+link
               
               email_subject="Activate your account"
               email_body="Hello, "+user.username+"\nPlease use this link to verify your account\n"+ activate_url
               email = EmailMessage(
                    email_subject,
                    email_body,
                    settings.DEFAULT_FROM_EMAIL,
                    [user_email],
    
                )
               try:
                   email.send(fail_silently=False)
                   messages.success(request, 'Account created successfully. Please check your email.')
               except Exception as e:
                    messages.error(request, f'Failed to send email: {e}')
            #    messages.success(request, 'Account created succesfully')
       return render(request, 'authentication/register.html')
   
class ActivationView(View):
    def get(self, request, uidb64, token):
        try:
            id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=id)
            if not token_generator.check_token(user, token):
                return redirect('login'+'?message='+'User already activated')
            
            if user.is_active:
                return redirect('login')
            user.is_active = True
            user.save()
            messages.success(request, 'Activation Successful, Login')
            return redirect('login')
        
        except Exception as e:
            messages.error(request, f'Something went wrong: {e}')
            
        return redirect('login')
      
class SetNewPasswordView(View):
    def get(self, request):
        return render(request, 'authentication/set-new-password.html')
    
class ResetPasswordView(View):
    def get(self, request):
        return render(request, 'authentication/reset-password.html')