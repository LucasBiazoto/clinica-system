from django.core.management.base import BaseCommand
from datetime import date, timedelta
from collections import defaultdict

from agenda.models import Consulta
from agenda.whatsapp import enviar_whatsapp


class Command(BaseCommand):
    help = 'Envia lembretes de consultas para o dia seguinte'

    def handle(self, *args, **kwargs):
        amanha = date.today() + timedelta(days=1)

        consultas = Consulta.objects.filter(
            data=amanha,
            tipo='consulta',
            lembrete_enviado=False
        )

        consultas_por_paciente = defaultdict(list)

        for consulta in consultas:
            if consulta.paciente and consulta.paciente.telefone:
                consultas_por_paciente[consulta.paciente].append(consulta)

        for paciente, lista_consultas in consultas_por_paciente.items():

            mensagem = f"""
Olá {paciente.nome} 👋

🔔 Você tem consulta(s) amanhã!

"""

            for c in lista_consultas:
                mensagem += f"📅 {c.data} às {c.hora}\n"

            mensagem += """

Responda:
1️⃣ SIM para confirmar
2️⃣ NÃO para cancelar
"""

            try:
                enviar_whatsapp(paciente.telefone, mensagem)

                for c in lista_consultas:
                    c.lembrete_enviado = True
                    c.save()

                self.stdout.write(self.style.SUCCESS(
                    f"Lembrete enviado para {paciente.nome}"
                ))

            except Exception as e:
                self.stdout.write(self.style.ERROR(
                    f"Erro ao enviar para {paciente.nome}: {e}"
                ))