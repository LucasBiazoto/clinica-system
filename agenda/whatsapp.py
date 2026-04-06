from .whatsapp import enviar_whatsapp
from django.shortcuts import redirect
from .models import ConversaWhatsApp


def responder_conversa(request, paciente_id):
    if request.method == 'POST':
        mensagem = request.POST.get('mensagem')

        conversa = ConversaWhatsApp.objects.filter(
            paciente__id=paciente_id
        ).last()

        if conversa:
            numero = conversa.paciente.telefone

            # 🔥 ENVIO REAL
            enviado = enviar_whatsapp(numero, mensagem)

            if enviado:
                conversa.resposta = mensagem
                conversa.save()
            else:
                print("Falha ao enviar mensagem")

    return redirect('painel')