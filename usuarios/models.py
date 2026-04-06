from django.db import models
from django.contrib.auth.models import User


class Clinica(models.Model):
    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20, blank=True, null=True)

    # 🎨 tema
    cor_primaria = models.CharField(max_length=20, default="#e91e63")
    cor_secundaria = models.CharField(max_length=20, default="#d4af37")

    def __str__(self):
        return self.nome


class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    clinica = models.ForeignKey(Clinica, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.clinica.nome}"