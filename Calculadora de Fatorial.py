Fatorial = float(input("Informe um número:"))
Resultado = Fatorial
while Fatorial > 1:
    Fatorial = Fatorial - 1
    Resultado = Resultado*Fatorial
print(int(Resultado))