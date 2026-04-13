from django.db import models

class ConversaWhatsapp(models.Model):
    numero = models.CharField(max_length=20)
    mensagem = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.numero} - {self.data}"