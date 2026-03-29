from django.contrib import admin
from .models import ConversaWhatsApp, ConfiguracaoIA, RespostaFAQ


@admin.register(ConversaWhatsApp)
class ConversaAdmin(admin.ModelAdmin):
    list_display = ('telefone', 'etapa', 'criado_em')


@admin.register(ConfiguracaoIA)
class ConfiguracaoIAAdmin(admin.ModelAdmin):
    list_display = ('nome_ia',)


@admin.register(RespostaFAQ)
class RespostaFAQAdmin(admin.ModelAdmin):
    list_display = ('pergunta',)