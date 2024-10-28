'''
Calcula la potencia, con la base y el exponente; pueden ocurrir tres cosas:
1. El exponente sea positivo, sólo tienes que imprimir la potencia.
2. El exponente sea 0, el resultado es 1.
3. El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.
Entrada:
    valorBase int -> b
    valorExponente int -> e
Salida:
    resultadoPotencia int -> p
'''
b = int(input("Base: "))
e = int(input("Exponente: "))

if e > 0:
    p = b ** e
elif e == 0:
    p = 1
elif e < 0:
    p_pre = b**e
    p = 1 / (p_pre * -1)
    p = f"{p:.0f}"

print(f"{b} ^ {e} = {p}")