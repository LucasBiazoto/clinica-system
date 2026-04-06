from django.db import models
from usuarios.models import Clinica

class Paciente(models.Model):
    clinica = models.ForeignKey(Clinica, on_delete=models.CASCADE)

    nome = models.CharField(max_length=200, blank=True, null=True)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.telefone