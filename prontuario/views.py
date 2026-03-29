from django.shortcuts import render, redirect, get_object_or_404
from .models import Prontuario
from usuarios.models import Paciente, Medico


def criar_prontuario(request, paciente_id):

    paciente = get_object_or_404(Paciente, id=paciente_id)

    if request.method == "POST":

        medico_id = request.POST.get("medico")
        queixa = request.POST.get("queixa")
        diagnostico = request.POST.get("diagnostico")
        tratamento = request.POST.get("tratamento")

        medico = Medico.objects.get(id=medico_id)

        Prontuario.objects.create(
            paciente=paciente,
            medico=medico,
            queixa_principal=queixa,
            diagnostico=diagnostico,
            tratamento=tratamento
        )

        return redirect("paciente_historico", paciente_id=paciente.id)

    medicos = Medico.objects.all()

    return render(request, "criar_prontuario.html", {
        "paciente": paciente,
        "medicos": medicos
    })