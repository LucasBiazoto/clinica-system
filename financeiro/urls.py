from django.urls import path
from .views import financeiro_lista, criar_movimento

urlpatterns = [

    path('', financeiro_lista, name="financeiro"),

    path('novo/', criar_movimento, name="criar_movimento"),

]
