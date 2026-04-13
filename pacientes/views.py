from django.shortcuts import render, redirect, get_object_or_404
from .models import Paciente


def lista_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'pacientes/lista.html', {'pacientes': pacientes})


def criar_paciente(request):
    if request.method == 'POST':
        Paciente.objects.create(
            nome=request.POST.get('nome'),
            email=request.POST.get('email'),
            telefone=request.POST.get('telefone'),
            data_nascimento=request.POST.get('data_nascimento')
        )
        return redirect('lista_pacientes')

    return render(request, 'pacientes/criar.html')


def editar_paciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)

    if request.method == 'POST':
        paciente.nome = request.POST.get('nome')
        paciente.email = request.POST.get('email')
        paciente.telefone = request.POST.get('telefone')
        paciente.data_nascimento = request.POST.get('data_nascimento')
        paciente.save()
        return redirect('lista_pacientes')

    return render(request, 'pacientes/editar.html', {'paciente': paciente})


def deletar_paciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    paciente.delete()
    return redirect('lista_pacientes')