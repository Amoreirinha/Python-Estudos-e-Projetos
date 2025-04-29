from datetime import datetime
from dateutil.relativedelta import relativedelta

agora = datetime.now()
namoro = datetime.strptime("24/04/2023", "%d/%m/%Y")
diferenca = relativedelta(agora, namoro)
print(f"Vocês estão juntos a {diferenca.years} anos, {diferenca.months} meses, {diferenca.days} dias, {diferenca.hours} horas, {diferenca.minutes} minutos e {diferenca.seconds} segundos.\n")