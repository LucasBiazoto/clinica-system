from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.messaging_response import MessagingResponse


@csrf_exempt
def webhook_whatsapp(request):
    if request.method == "POST":
        try:
            # 📩 Dados recebidos do Twilio
            mensagem = request.POST.get('Body', '').strip().lower()
            numero = request.POST.get('From', '')

            print("=== NOVA MENSAGEM ===")
            print("Telefone:", numero)
            print("Mensagem:", mensagem)

            # 🤖 Cria resposta Twilio
            resposta = MessagingResponse()

            # 💬 Lógica simples (sem erro)
            if mensagem in ["oi", "ola", "olá"]:
                resposta.message("Olá! 👋 Bem-vindo à clínica.\nComo posso te ajudar?")
            
            elif "consulta" in mensagem:
                resposta.message("Para agendar uma consulta, me informe seu nome completo 📅")
            
            elif "horario" in mensagem or "horário" in mensagem:
                resposta.message("Nosso horário é de segunda a sexta, das 08h às 18h 🕒")
            
            else:
                resposta.message("Não entendi 🤔\nDigite:\n- oi\n- consulta\n- horario")

            # ✅ Retorno obrigatório para Twilio
            return HttpResponse(str(resposta), content_type="text/xml")

        except Exception as e:
            print("ERRO:", str(e))
            return HttpResponse("Erro interno", status=500)

    return HttpResponse("Método não permitido", status=405)