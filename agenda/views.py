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

            try:
                # 🤖 TENTA USAR IA
                completion = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "Você é um atendente de clínica médica educado e direto."},
                        {"role": "user", "content": mensagem}
                    ]
                )

                reply = completion.choices[0].message.content

            except Exception as e:
                # ⚠️ FALLBACK AUTOMÁTICO
                print("ERRO OPENAI:", str(e))

                if "oi" in mensagem.lower():
                    reply = "Olá! 👋 Como posso te ajudar?\nDigite: consulta, horário ou exames."
                
                elif "consulta" in mensagem.lower():
                    reply = "Para agendar uma consulta, me informe seu nome completo 📅"
                
                elif "horario" in mensagem.lower() or "horário" in mensagem.lower():
                    reply = "Atendemos de segunda a sexta, das 08h às 18h 🕒"
                
                else:
                    reply = "No momento estou sem IA 🤖, mas posso te ajudar.\nDigite: consulta"

            resposta.message(reply)

            return HttpResponse(str(resposta), content_type="text/xml")

        except Exception as e:
            print("ERRO GERAL:", str(e))

            resposta = MessagingResponse()
            resposta.message("Erro no servidor 😢 tente novamente")

            return HttpResponse(str(resposta), content_type="text/xml")

    return HttpResponse("Método não permitido", status=405)