from openai import OpenAI
from django.conf import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)


def gerar_resposta(mensagem):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Você é uma atendente de clínica estética, educada e objetiva."},
                {"role": "user", "content": mensagem}
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        print("Erro IA:", e)
        return "Desculpe, tivemos um erro. Um atendente irá te ajudar."


def eh_agendamento(mensagem):
    palavras = ["agendar", "horário", "consulta", "marcar"]

    mensagem = mensagem.lower()

    return any(p in mensagem for p in palavras)