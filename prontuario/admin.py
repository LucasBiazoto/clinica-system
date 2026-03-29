from django.contrib import admin
from .models import Prontuario


@admin.register(Prontuario)
class ProntuarioAdmin(admin.ModelAdmin):

    list_display = ("paciente", "medico", "data")

    search_fields = ("paciente__nome", "medico__nome")

    list_filter = ("medico", "data")