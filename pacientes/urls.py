from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_pacientes, name='lista_pacientes'),
    path('novo/', views.criar_paciente, name='criar_paciente'),
    path('editar/<int:id>/', views.editar_paciente, name='editar_paciente'),
    path('deletar/<int:id>/', views.deletar_paciente, name='deletar_paciente'),
]