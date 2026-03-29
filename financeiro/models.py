from django.db import models
from usuarios.models import Clinica


class Financeiro(models.Model):

    clinica = models.ForeignKey(
        Clinica,
        on_delete=models.CASCADE
    )

    descricao = models.CharField(max_length=200)

    valor = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    tipo = models.CharField(
        max_length=20,
        choices=[
            ("ENTRADA","Entrada"),
            ("SAIDA","Saída")
        ]
    )

    data = models.DateField()

    def __str__(self):

        return self.descricao
