from django.shortcuts import render
from usuarios.models import Paciente
from financeiro.models import Financeiro
from django.db.models import Sum
from datetime import date


def dashboard(request):

    hoje = date.today()

    consultas_hoje = Consulta.objects.filter(
        data=hoje
    ).count()

    total_pacientes = Paciente.objects.count()

    faturamento_total = Financeiro.objects.aggregate(
        total=Sum("valor")
    )["total"] or 0

    faturamento_hoje = Financeiro.objects.filter(
        data=hoje
    ).aggregate(
        total=Sum("valor")
    )["total"] or 0

    consultas_mes = []

    for i in range(1, 13):

        total = Consulta.objects.filter(
            data__month=i
        ).count()

        consultas_mes.append(total)

    context = {

        "consultas_hoje": consultas_hoje,
        "total_pacientes": total_pacientes,
        "faturamento_total": faturamento_total,
        "faturamento_hoje": faturamento_hoje,
        "consultas_mes": consultas_mes

    }

    return render(request, "dashboard.html", context)
