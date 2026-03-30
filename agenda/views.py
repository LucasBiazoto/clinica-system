from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.messaging_response import MessagingResponse
import os
from openai import OpenAI

client = OpenAI()


@csrf_exempt
def webhook_whatsapp(request):
    if request.method == "POST":
        try:
            mensagem = request.POST.get('Body', '').strip()
            numero = request.POST.get('From', '')

            print("=== NOVA MENSAGEM ===")
            print("Telefone:", numero)
            print("Mensagem:", mensagem)

            resposta = MessagingResponse()

            # 🔥 chamada simples e compatível
            completion = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "Você é um atendente de clínica educado e direto."},
                    {"role": "user", "content": mensagem}
                ]
            )

            reply = completion.choices[0].message.content

            resposta.message(reply)

            return HttpResponse(str(resposta), content_type="text/xml")

        except Exception as e:
            print("ERRO DETALHADO:", str(e))

            resposta = MessagingResponse()
            resposta.message("Erro no servidor 😢")

            return HttpResponse(str(resposta), content_type="text/xml")

    return HttpResponse("Método não permitido", status=405)