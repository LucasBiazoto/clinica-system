from django.urls import path
from .views import (
    login_view,
    logout_view,
    lista_pacientes,
    lista_medicos,
    criar_medico
)

urlpatterns = [

    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),

    path("pacientes/", lista_pacientes, name="pacientes"),

    path("medicos/", lista_medicos, name="medicos"),

    path("criar-medico/", criar_medico, name="criar_medico"),

]
