from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Perfil, Clinica


@receiver(post_save, sender=User)
def criar_perfil(sender, instance, created, **kwargs):
    if created:
        clinica = Clinica.objects.first()
        if clinica:
            Perfil.objects.create(user=instance, clinica=clinica)