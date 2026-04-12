from django.db import models

class Paciente(models.Model):
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome