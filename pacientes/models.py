from django.db import models


class Paciente(models.Model):
    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)  # 🔥 IMPORTANTE
    email = models.EmailField(blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nome