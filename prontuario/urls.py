from django.urls import path
from .views import criar_prontuario

urlpatterns = [

    path("novo/<int:paciente_id>/", criar_prontuario, name="criar_prontuario"),

]