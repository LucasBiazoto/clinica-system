from django.urls import path
from . import views

urlpatterns = [
    path("webhook/whatsapp/", views.webhook_whatsapp, name="webhook_whatsapp"),

    path("painel/", views.painel_atendimento, name="painel"),
    path("chat/<int:paciente_id>/", views.visualizar_conversa, name="visualizar_conversa"),
    path("responder/<int:paciente_id>/", views.responder_conversa, name="responder_conversa"),
    path("finalizar/<int:paciente_id>/", views.finalizar_conversa, name="finalizar_conversa"),
]