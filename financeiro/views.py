from django.shortcuts import render, redirect
from django.db.models import Sum
from datetime import date
from .models import Financeiro


def financeiro_lista(request):

    clinica = request.user.perfil.clinica

    registros = Financeiro.objects.filter(
        clinica=clinica
    ).order_by("-data")

    total = registros.aggregate(
        total=Sum("valor")
    )["total"] or 0

    return render(request, "financeiro.html", {
        "registros": registros,
        "total": total
    })


def criar_movimento(request):

    clinica = request.user.perfil.clinica

    if request.method == "POST":

        descricao = request.POST.get("descricao")
        valor = request.POST.get("valor")
        tipo = request.POST.get("tipo")

        Financeiro.objects.create(
            clinica=clinica,
            descricao=descricao,
            valor=valor,
            tipo=tipo,
            data=date.today()
        )

        return redirect("financeiro")

    return render(request, "financeiro_criar.html")
