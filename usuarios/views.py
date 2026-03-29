from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Paciente


def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:

            login(request, user)
            return redirect("dashboard")

    return render(request, "login.html")


def logout_view(request):

    logout(request)
    return redirect("login")


def lista_pacientes(request):

    clinica = request.user.perfil.clinica

    pacientes = Paciente.objects.filter(
        clinica=clinica
    )

    return render(request, "pacientes.html", {
        "pacientes": pacientes
    })

from .models import Medico


def lista_medicos(request):

    clinica = request.user.perfil.clinica

    medicos = Medico.objects.filter(
        clinica=clinica
    )

    return render(request, "medicos.html", {
        "medicos": medicos
    })


def criar_medico(request):

    clinica = request.user.perfil.clinica

    if request.method == "POST":

        nome = request.POST.get("nome")
        especialidade = request.POST.get("especialidade")
        telefone = request.POST.get("telefone")

        Medico.objects.create(
            clinica=clinica,
            nome=nome,
            especialidade=especialidade,
            telefone=telefone
        )

        return redirect("medicos")

    return render(request, "criar_medico.html")

