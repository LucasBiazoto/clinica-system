from .models import Perfil, Clinica

def get_clinica(request):
    perfil, _ = Perfil.objects.get_or_create(
        user=request.user,
        defaults={'clinica': Clinica.objects.first()}
    )
    return perfil.clinica