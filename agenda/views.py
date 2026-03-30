from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.messaging_response import MessagingResponse
from .models import ConversaWhatsApp, ConfiguracaoIA, RespostaFAQ

from openai import OpenAI
import os

# 🔑 cliente OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def buscar_resposta_faq(mensagem):
    mensagem = mensagem.lower()
    respostas = RespostaFAQ.objects.all()

    for item in respostas:
        if item.pergunta.lower() in mensagem:
            return item.resposta

    return None


@csrf_exempt
def webhook_whatsapp(request):
    if request.method == 'POST':

        mensagem = request.POST.get('Body', '').strip()
        telefone = request.POST.get('From', '')

        print("📲 NOVA MENSAGEM")
        print(f"Telefone: {telefone}")
        print(f"Mensagem: {mensagem}")

        # 🔍 DEBUG
        print("🔑 OPENAI KEY:", os.getenv("OPENAI_API_KEY"))

        conversa, created = ConversaWhatsApp.objects.get_or_create(
            telefone=telefone
        )

        # 🔑 CONFIG IA
        config = ConfiguracaoIA.objects.first()

        if not config:
            nome_ia = "Sofia"
            tom = "Responda de forma educada e profissional."
        else:
            nome_ia = config.nome_ia
            tom = config.tom

        resp = MessagingResponse()

        # 🔁 INICIO
        if conversa.etapa == 'inicio':
            resp.message(
                f"Olá! 👋\n"
                f"Sou a {nome_ia}, assistente virtual da clínica 😊\n\n"
                "Digite:\n"
                "1 - Agendar consulta\n"
                "2 - Tirar dúvidas"
            )
            conversa.etapa = 'menu'

        # 📋 MENU
        elif conversa.etapa == 'menu':
            if mensagem == '1':
                resp.message(
                    "Perfeito! 👩‍⚕️\n"
                    "Vou te encaminhar para nossa atendente.\n"
                    "Aguarde um instante..."
                )
                conversa.etapa = 'humano'

            elif mensagem == '2':
                resp.message("Pode me perguntar 😊")
                conversa.etapa = 'ia'

            else:
                resp.message("❌ Opção inválida.\nDigite 1 ou 2.")

        # 🤖 IA
        elif conversa.etapa == 'ia':

            resposta_faq = buscar_resposta_faq(mensagem)

            if resposta_faq:
                resp.message(resposta_faq)

            else:
                try:
                    resposta_ia = client.chat.completions.create(
                        model="gpt-4o-mini",
                        messages=[
                            {
                                "role": "system",
                                "content": (
                                    f"Você é a {nome_ia}, assistente virtual de uma clínica. "
                                    f"{tom} "
                                    "Nunca dê diagnósticos médicos. "
                                    "Se não souber, diga que um atendente irá ajudar."
                                )
                            },
                            {
                                "role": "user",
                                "content": mensagem
                            }
                        ],
                        max_tokens=150
                    )

                    resposta = resposta_ia.choices[0].message.content

                    print("🤖 RESPOSTA IA:", resposta)

                    resp.message(resposta)

                except Exception as e:
                    print("🔥 ERRO OPENAI:")
                    print(str(e))

                    resp.message(
                        "Não consegui te responder agora 😕\n"
                        "Vou te encaminhar para nossa atendente."
                    )
                    conversa.etapa = 'humano'

        # 👩‍⚕️ HUMANO
        elif conversa.etapa == 'humano':
            resp.message(
                "👩‍⚕️ Nossa atendente irá te responder em breve.\n"
                "Por favor aguarde."
            )

        conversa.save()

        return HttpResponse(str(resp), content_type='application/xml')

    return HttpResponse("Método não permitido", status=405)