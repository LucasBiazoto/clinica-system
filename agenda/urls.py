from django.urls import path
from .views import webhook_whatsapp

urlpatterns = [
    path('webhook/whatsapp/', webhook_whatsapp),
]