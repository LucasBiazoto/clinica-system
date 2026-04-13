from django.http import HttpResponse
from .models import ConversaWhatsapp


def webhook_whatsapp(request):
    if request.method == 'POST':
        numero = request.POST.get('From')
        mensagem = request.POST.get('Body')

        ConversaWhatsapp.objects.create(
            numero=numero,
            mensagem=mensagem
        )

        return HttpResponse("Recebido com sucesso 🚀")

    return HttpResponse("OK")