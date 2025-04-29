# Projeto
# Calculadora de mercadinho usando dicionários
# Criar um programa onde, dentre um dicionário com os produtos cadastrados, eu coloque o código do produto e a quantidade e ele some tudo no final.
# Pedir nome do Cliente.
# Colocar uma função para retirar um produto caso colocado errado.
# Colocar opções de pagamento no final.
# Calcular troco no caso de dinheiro.
# Dar preferências por usar funções lambda.
# Futuramente criar versão com unidade de medidas para cálculo automático de preço. Exemplos: Carne, Granel, Pão etc..
# Tentar criar um sistema para adicionar um novo produto usando input e append.
# Como resultado final, printar o nome do cliente, os produtos + quantidade + Subtotal, Total da Compra, Forma de pagamento.

produtos = {
"G01":["Guaraná Antártica lata     ",5],
"G02":["Guaraná Antártica Zero lata",5.5],
"P01":["Pipoca 1kg                 ",3.9],
"PA1":["Pão de Sal unidade         ",1],
"PA2":["Pão Doce unidade           ",1.25],
"L01":["Leite 1L                   ",3.45],
"L02":["Leite Desnatado 1L         ",4.65],
"L03":["Leite Sem Lactose 1L       ",5.26],
"A01":["Açúcar 1kg                 ",8],
"AR1":["Arroz 5kg                  ",4.5]
            }

nomedomercado = "Donavan"
extrato={}
conta = 0
nome = ""
moeda = "R$"

def inicio():
    global nome,moeda
    print(f"Bem vindo ao Mercadinho {nomedomercado}\n")
    print("Nossos produtos são:\n")
    print(f"Código do Produto:\t|Produto:\t\t\t|Valor ({moeda}):\n")
    for key, value in produtos.items():
        nome_produto = value[0]
        valor_produto = value[1]
        print(f"{key}\t\t\t|{nome_produto}\t|{valor_produto}")
    decisao1=str(input("\n\nGostaria de comprar algum produto? Digite 's' para sim e 'n' para não.\n"))
    if decisao1 == "s":
        nome=str(input("Digite seu nome completo:\n"))
        compras()
    elif decisao1 == "admincode":
        add_produto()
    else:
        adeus()

def compras():
    global conta, extrato
    compra=str(input("\n\nDigite o código do produto a ser comprado:\n"))
    produto=produtos[compra][0]
    quantidade=int(input(f"Digite a quantidade do produto {produto}\n"))
    valor = produtos[compra][1]
    item = valor*quantidade
    conta += item
    extrato[compra] = [produto,quantidade,valor,item]
    adicionar_ao_carrinho()

def adicionar_ao_carrinho():
    global nome, conta, extrato, moeda
    decisao2=str(input("Deseja adicionar mais um item? Digite 's' para sim e 'n' para não.\n"))
    if decisao2=="s":
        compras()
    else:
        print(f"\n\n__________________________________________________________________________\n\n\n\t{nome}")
        print("\nCódigo:\t|Produto:\t\t\t|Quantidade:\t|Valor unit.:\t|Subtotal:\n")
        for key, value in extrato.items():
            produto = value[0]
            quantidade = value[1]
            valor = value[2]
            subtotal = value[3]
            print(f"{key}\t|{produto}\t|{quantidade}\t\t|{valor}\t\t|{subtotal}")
        print(f"\n\nTotal:\t\t{moeda,conta}\n")
        print(f"\n\n__________________________________________________________________________\n")

        nome=""
        conta=0
        extrato={}
        nova_compra()

def nova_compra():
    decisao3=str(input("\nDeseja realizar uma nova compra? Digite 's' para sim e 'n' para não.\n "))
    if decisao3=="s":
        inicio()
    else:
        adeus()

def add_produto():
    print(2)

def adeus():
    print("\n\nAdeus!!\n\n")

inicio()