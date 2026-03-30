from twilio.rest import Client

ACCOUNT_SID = 'SEU_SID'
AUTH_TOKEN = 'SEU_TOKEN'

client = Client(ACCOUNT_SID, AUTH_TOKEN)


def enviar_whatsapp(telefone, mensagem):
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=mensagem,
        to=f'whatsapp:{telefone}'
    )

    print("WhatsApp enviado com sucesso!")
    print("SID:", message.sid)  