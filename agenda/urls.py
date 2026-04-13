from django.urls import path
from . import views
from .whatsapp import webhook_whatsapp

urlpatterns = [
    path('', views.home, name='home'),
    path('webhook/whatsapp/', webhook_whatsapp, name='webhook_whatsapp'),
]