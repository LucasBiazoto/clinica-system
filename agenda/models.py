from django.db import models


class ConversaWhatsApp(models.Model):
    telefone = models.CharField(max_length=20)
    etapa = models.CharField(max_length=50, default='inicio')

    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.telefone


class ConfiguracaoIA(models.Model):
    nome_ia = models.CharField(max_length=50, default="Sofia")
    tom = models.TextField(
        default="Responda de forma educada, profissional e acolhedora."
    )

    def __str__(self):
        return self.nome_ia


class RespostaFAQ(models.Model):
    pergunta = models.CharField(max_length=100)
    resposta = models.TextField()

    def __str__(self):
        return self.pergunta