#calculadora de idade e afins
from datetime import datetime
from dateutil.relativedelta import relativedelta

def inicio():
    start = input("Começar o programa?(y/n)\n")
    if start == "y":
        programa()
    else:
        print("Adeus\n") 

def programa():
    nascimento_str = input("Insira sua data de nascimento no formato dd/mm/aaaa: ")

    agora = datetime.now()

    nascimento = datetime.strptime(nascimento_str, "%d/%m/%Y")

    diferenca = relativedelta(agora, nascimento)

    diferencadias = agora - nascimento

    dindin = diferencadias.days*24*60*60*10

    dindinsalariominimo = int(dindin/1518)

    dindinmeses = int(dindin/2979)

    dindinanos = int(dindinmeses/12)

    torredindin10 = int(float(dindin)*0.00011)

    torrebujicalifa = int(torredindin10/828)

    print(f"Você tem {diferenca.years} anos, {diferenca.months} meses, {diferenca.days} dias, {diferenca.hours} horas, {diferenca.minutes} minutos e {diferenca.seconds} segundos.\n")

    print(f"Você viveu {diferenca.years} anos aproximadamente.\n")

    print(f"Você viveu {diferenca.years*12+diferenca.months} meses aproximadamente.\n")

    print(f"Você viveu {diferencadias.days} dias aproximadamente.\n")

    print(f"Você viveu {diferencadias.days*24} horas aproximadamente.\n")

    print(f"Você viveu {diferencadias.days*24*60} minutos aproximadamente.\n")

    print(f"Você viveu {diferencadias.days*24*60*60} segundos aproximadamente.\n")

    print(f"Caso você ganhasse 10 reais por segundo, você teria {dindin} reais.\n")

    print(f"Isso seria equivalente a {dindinsalariominimo} salários mínimos.\n")

    print(f"Uma pessoa que ganha o salário médio brasileiro (R$2.979,00) demoraria {dindinmeses} meses , ou aproximadamente {dindinanos } anos, para conseguir juntar esse dinheiro.\n")

    print(f"Considerando o que os filhos dessa pessoa ganhassem o mesmo que ela e continuassem trabalhando para juntar essa quantia, seria necessário {int(dindinanos/30)} gerações para juntar esse dinheiro.\n")

    print(f'Caso fizessemos uma torre de notas de 10 reais com esse dinheiro, teríamos uma torre com altura de {torredindin10} metros\n')

    print(f"Esta torre seria equivalente a {torrebujicalifa} Burj Khalifa's.\n")

    if 80000000>dindin>45000000:
        print("Você seria mais rico que o Roberto Justus\n")
    elif 105000000>dindin>80000000:
        print("Você seria mais rico que o Daniela Mercury\n")
    elif 120000000>dindin>105000000:
        print("Você seria mais rico que o Ana Maria Braga\n")
    elif 270000000>dindin>120000000:
        print("Você seria mais rico que o Chitãozinho e Xororó\n")
    elif 350000000>dindin>270000000:
        print("Você seria mais rico que o Gisele Bundchen\n")
    elif 500000000>dindin>350000000:
        print("Você seria mais rico que o Ivete Sangalo\n")
    elif 750000000>dindin>500000000:
        print("Você seria mais rico que o Pelé\n")
    elif 950000000>dindin>750000000:
        print("Você seria mais rico que o Xuxa\n")
    elif 1900000000>dindin>950000000:
        print("Você seria mais rico que o Falstão\n")
    elif 28690000000>dindin>1900000000:
        print("Você seria mais rico que o Silvio Santos\n")
    if dindin>28690000000:
        print("Você estaria entre as top 10 pessoas mais ricos do Brasil\n")
    else:
        print("Você não estaria entre as top 10 pessoas mais ricas do Brasil\n")
    restart()

def restart():
    restart = input('Gostaria de recomeçar?(y/n)\n')
    if restart == "y":
        inicio()
    else:
        print("Adeus\n")

inicio()

