from django.db import models
from usuarios.models import Paciente, Medico


class Prontuario(models.Model):

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)

    data = models.DateTimeField(auto_now_add=True)

    queixa_principal = models.TextField()

    historico = models.TextField()

    diagnostico = models.TextField()

    tratamento = models.TextField()

    observacoes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.paciente.nome} - {self.data}"