#calculadora básica

import math
from datetime import datetime
from dateutil.relativedelta import relativedelta

def inicio():
    print("Bem vindo a calculadora Python\n")
    recomeco()

def recomeco():
    start = input("Qual operação você gostaria de realizar?\n1. Adição\n2. Subtração\n3. Divisão\n4. Multiplicação\n5. Fatorial\n6. Potenciação\n7. Raiz Quadrada\n8. Raiz Cúbica\n9. Calculadora de tempo de namoro\n\n0. Fechar Calculadora\n\nDigite o número da operação a ser seguida:")
    if start == "1":
        adição()
    elif start == "2":
        subtracao()
    elif start == "3":
        divisao()
    elif start == "4":
        multiplicacao()
    elif start == "5":
        fatorial()
    elif start == "6":
        potenciacao()
    elif start == "7":
        RaizQuadrada()
    elif start == "8":
        RaizCubica()
    elif start == "9":
        datanamoro()
    elif start == "0":
        print("Adeus")

def perguntar_reinicio():
    restart = input("Gostaria de realizar outra operação? (y/n)\n")
    if restart == "y":
        recomeco()
    else:
        print('Adeus\n')

def doisnum():
    num1 = float(input('Digite o primeiro número:\n'))
    num2 = float(input('Digite o segundo número:\n'))
    return num1, num2

def adição():
    num1, num2 = doisnum()
    print(f'{num1} + {num2} = {num1+num2}\n')
    perguntar_reinicio()

def subtracao():
    num1, num2 = doisnum()
    print(f'{num1} - {num2} = {num1-num2}\n')
    perguntar_reinicio()

def multiplicacao():
    num1, num2 = doisnum()
    print(f'{num1} x {num2} = {num1*num2}\n')
    perguntar_reinicio()

def divisao():
    num1, num2 = doisnum()
    if num2 == 0:
        print("ERROR - Divisão por zero")
        divisao()
    else:
        print(f'{num1} / {num2} = {num1/num2}\n')
        perguntar_reinicio()

def fatorial():
    nfato = int(input('Digite o número:\n'))
    if nfato < 0:
            print("Erro: Fatorial de número negativo não é definido. Tente novamente.\n")
            fatorial()
    else:
        print(f'Fatorial de {nfato} = {math.factorial(nfato)}\n')
        perguntar_reinicio()

def potenciacao():
    num1, num2 = doisnum()
    print(f'{num1} elevado a {num2} = {num1**num2}\n')
    perguntar_reinicio()

def RaizQuadrada():
    nrq=float(input("Digite um número:\n"))
    print(f'Raiz Quadrada de {nrq} é {math.sqrt(nrq)}\n')
    perguntar_reinicio()

def RaizCubica():
    nrc=float(input("Digite um número:\n"))
    print(f'Raiz Cúbica de {nrc} é {math.cbrt(nrc)}\n')
    perguntar_reinicio()

def datanamoro():
    agora = datetime.now()
    datanamorando = input("Informe a data de ínicio do namoro (dd/mm/aaaa):")
    namoro = datetime.strptime(datanamorando, "%d/%m/%Y")
    diferenca = relativedelta(agora, namoro)
    print(f"\nVocês estão juntos a {diferenca.years} anos, {diferenca.months} meses, {diferenca.days} dias, {diferenca.hours} horas, {diferenca.minutes} minutos e {diferenca.seconds} segundos.\n")
    perguntar_reinicio()

inicio()