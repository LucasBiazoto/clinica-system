from django.contrib.auth.models import User
from django.db import models


class Clinica(models.Model):

    nome = models.CharField(max_length=200)

    cnpj = models.CharField(max_length=20, blank=True)

    telefone = models.CharField(max_length=20, blank=True)

    email = models.EmailField(blank=True)

    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.nome


class Perfil(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    clinica = models.ForeignKey(
        Clinica,
        on_delete=models.CASCADE,
        null=True
    )

    tipo = models.CharField(
        max_length=20,
        choices=[
            ("ADMIN", "Administrador"),
            ("RECEPCAO", "Recepção"),
            ("MEDICO", "Médico")
        ]
    )

    def __str__(self):

        return f"{self.user.username} - {self.clinica}"


class Paciente(models.Model):

    clinica = models.ForeignKey(Clinica, on_delete=models.CASCADE)

    nome = models.CharField(max_length=200)

    telefone = models.CharField(max_length=20)

    email = models.EmailField(blank=True)

    data_nascimento = models.DateField(blank=True, null=True)

    def __str__(self):

        return self.nome


class Medico(models.Model):

    clinica = models.ForeignKey(Clinica, on_delete=models.CASCADE)

    nome = models.CharField(max_length=200)

    especialidade = models.CharField(max_length=200)

    telefone = models.CharField(max_length=20)

    def __str__(self):

        return self.nome
