from django.contrib.auth.decorators import login_required
from django.shortcuts import render  # 👈 FALTAVA ISSO
from pacientes.models import Paciente


@login_required(login_url='/usuarios/login/')
def home(request):
    total_pacientes = Paciente.objects.count()

    return render(request, 'home.html', {
        'total_pacientes': total_pacientes
    })