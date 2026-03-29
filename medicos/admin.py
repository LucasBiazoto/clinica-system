from django.contrib import admin
from .models import Medico


@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):

    list_display = ("id", "nome", "especialidade")

    search_fields = ("nome", "especialidade")