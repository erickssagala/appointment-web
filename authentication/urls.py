from django.urls import path
from .views import LoginView
from .views import RegisterView
from .views import ResetPasswordView
from .views import SetNewPasswordView


urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('register', RegisterView.as_view(), name='register'),
    path('reset-password', ResetPasswordView.as_view(), name='reset-password'),
    path('set-new-password', SetNewPasswordView.as_view(), name='set-new-password'),
]
