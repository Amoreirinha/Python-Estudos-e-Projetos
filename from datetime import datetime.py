from datetime import datetime
from dateutil.relativedelta import relativedelta

agora = datetime.now()

nascimento_str = input("Insira sua data de nascimento no formato dd/mm/aaaa: ")

nascimento = datetime.strptime(nascimento_str, "%d/%m/%Y")

diferenca = relativedelta(agora, nascimento)

diferencadias = agora - nascimento

dindin = diferencadias.days*24*60*60*10

dindinsalariominimo = int(dindin/1518)

dindinmeses = int(dindin/2979)

dindinanos = int(dindinmeses/12)

torredindin10 = int(float(dindin)*0.00011)

torrebujicalifa = int(torredindin10/828)


print(f"Você tem {diferenca.years} anos, {diferenca.months} meses, {diferenca.days} dias, {diferenca.hours} horas, {diferenca.minutes} minutos e {diferenca.seconds} segundos.")

print(f"Você viveu {diferenca.years} anos aproximadamente.")

print(f"Você viveu {diferenca.years*12+diferenca.months} meses aproximadamente.")

print(f"Você viveu {diferencadias.days} dias aproximadamente.")

print(f"Você viveu {diferencadias.days*24} horas aproximadamente.")

print(f"Você viveu {diferencadias.days*24*60} minutos aproximadamente.")

print(f"Você viveu {diferencadias.days*24*60*60} segundos aproximadamente.")

print(f"Caso você ganhasse 10 reais por segundo, você teria {dindin} reais.")

print(f"Isso seria equivalente a {dindinsalariominimo} salários mínimos.")

print(f"Uma pessoa que ganha o salário médio brasileiro (R$2.979,00) demoraria {dindinmeses} meses , ou aproximadamente {dindinanos } anos, para conseguir juntar esse dinheiro.")

print(f"Considerando o que os filhos dessa pessoa ganhassem o mesmo que ela e continuassem trabalhando para juntar essa quantia, seria necessário {int(dindinanos/30)} gerações para juntar esse dinheiro.")

print(f"Esta torre seria equivalente a {torrebujicalifa} Burj Khalifa's.")

if 80000000>dindin>45000000:
    print("Você seria mais rico que o Roberto Justus")
elif 105000000>dindin>80000000:
    print("Você seria mais rico que o Daniela Mercury")
elif 120000000>dindin>105000000:
    print("Você seria mais rico que o Ana Maria Braga")
elif 270000000>dindin>120000000:
    print("Você seria mais rico que o Chitãozinho e Xororó")
elif 350000000>dindin>270000000:
    print("Você seria mais rico que o Gisele Bundchen")
elif 500000000>dindin>350000000:
    print("Você seria mais rico que o Ivete Sangalo")
elif 750000000>dindin>500000000:
    print("Você seria mais rico que o Pelé")
elif 950000000>dindin>750000000:
    print("Você seria mais rico que o Xuxa")
elif 1900000000>dindin>950000000:
    print("Você seria mais rico que o Falstão")
elif 28690000000>dindin>1900000000:
    print("Você seria mais rico que o Silvio Santos")
if dindin>28690000000:
    print("Você estaria entre as top 10 pessoas mais ricos do Brasil")
else:
    print("Você não estaria entre as top 10 pessoas mais ricas do Brasil")