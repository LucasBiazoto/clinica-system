from django.db import models


class Medico(models.Model):

    nome = models.CharField(max_length=200)

    especialidade = models.CharField(max_length=200, blank=True)

    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.nome