from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from .models import ConversaWhatsApp
from pacientes.models import Paciente
from usuarios.models import Clinica


# =========================
# 🔹 WEBHOOK WHATSAPP
# =========================
@csrf_exempt
def webhook_whatsapp(request):
    if request.method == "POST":
        try:
            telefone = request.POST.get("From", "").replace("whatsapp:", "")
            mensagem = request.POST.get("Body", "").lower()

            clinica = Clinica.objects.first()
            if not clinica:
                return HttpResponse("""
                    <Response>
                        <Message>Clínica não configurada.</Message>
                    </Response>
                """, content_type="text/xml")

            paciente, _ = Paciente.objects.get_or_create(
                telefone=telefone,
                defaults={"clinica": clinica}
            )

            if not paciente.clinica:
                paciente.clinica = clinica
                paciente.save()

            if "agendamento" in mensagem:
                resposta = "Perfeito 😊 Vou te encaminhar para nosso atendimento humano."
            elif "oi" in mensagem or "olá" in mensagem:
                resposta = "Olá 😊 Em breve nossa equipe irá te atender."
            else:
                resposta = "Recebemos sua mensagem 😊"

            ConversaWhatsApp.objects.create(
                paciente=paciente,
                clinica=clinica,
                mensagem=mensagem,
                resposta=resposta
            )

            return HttpResponse(f"""
                <Response>
                    <Message>{resposta}</Message>
                </Response>
            """, content_type="text/xml")

        except Exception as e:
            print("ERRO REAL:", e)
            return HttpResponse("""
                <Response>
                    <Message>Erro interno. Tente novamente.</Message>
                </Response>
            """, content_type="text/xml")

    return HttpResponse("OK")


# =========================
# 🔹 PAINEL
# =========================
@login_required
def painel_atendimento(request):
    perfil = request.user.perfil
    clinica = perfil.clinica

    conversas = ConversaWhatsApp.objects.filter(
        clinica=clinica
    ).order_by("-criado_em")

    return render(request, "painel.html", {
        "conversas": conversas,
        "clinica": clinica
    })


# =========================
# 🔹 CHAT
# =========================
@login_required
def visualizar_conversa(request, paciente_id):
    paciente = Paciente.objects.filter(id=paciente_id).first()

    if not paciente:
        return redirect("painel")

    mensagens = ConversaWhatsApp.objects.filter(
        paciente=paciente
    ).order_by("criado_em")

    return render(request, "chat.html", {
        "paciente": paciente,
        "mensagens": mensagens
    })


# =========================
# 🔹 RESPONDER
# =========================
@login_required
def responder_conversa(request, paciente_id):
    paciente = Paciente.objects.filter(id=paciente_id).first()

    if not paciente:
        return redirect("painel")

    clinica = paciente.clinica

    if request.method == "POST":
        resposta = request.POST.get("resposta")

        ConversaWhatsApp.objects.create(
            paciente=paciente,
            clinica=clinica,
            mensagem="(humano)",
            resposta=resposta
        )

        return redirect("visualizar_conversa", paciente_id=paciente.id)

    return redirect("painel")


# =========================
# 🔹 FINALIZAR
# =========================
@login_required
def finalizar_conversa(request, paciente_id):
    paciente = Paciente.objects.filter(id=paciente_id).first()

    if paciente:
        ConversaWhatsApp.objects.filter(paciente=paciente).delete()

    return redirect("painel")