from django.urls import path
from .views import LoginView
from .views import RegisterView
from .views import ResetPasswordView
from .views import SetNewPasswordView
from .views import UsernameValidationView
from .views import EmailValidationView
from .views import ActivationView, LogoutView

from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    # path('home', HomeView.as_view(), name='home'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('login', LoginView.as_view(), name='login'),
    path('register', RegisterView.as_view(), name='register'),
    path('reset-password', ResetPasswordView.as_view(), name='reset-password'),
    path('set-new-password', SetNewPasswordView.as_view(), name='set-new-password'),
    path('validate-username', csrf_exempt(UsernameValidationView.as_view()), name='validate-username'),
    path('validate-email', csrf_exempt(EmailValidationView.as_view()), name='validate-email'),
    path('activate/<uidb64>/<token>', csrf_exempt(ActivationView.as_view()), name='activate'),
]
