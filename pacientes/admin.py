from django.contrib import admin
from .models import Paciente


@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):

    list_display = ("id", "nome", "telefone", "email", "data_nascimento")

    search_fields = ("nome", "telefone", "email")

    list_filter = ("data_nascimento",)