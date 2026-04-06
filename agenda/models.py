from django.db import models
from pacientes.models import Paciente
from usuarios.models import Clinica


class ConversaWhatsApp(models.Model):
    clinica = models.ForeignKey(Clinica, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

    mensagem = models.TextField()
    resposta = models.TextField(blank=True, null=True)

    quer_agendar = models.BooleanField(default=False)
    atendido = models.BooleanField(default=False)

    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.paciente.telefone} - {self.criado_em}"


class RespostaFAQ(models.Model):
    pergunta = models.CharField(max_length=255)
    resposta = models.TextField()

    def __str__(self):
        return self.pergunta