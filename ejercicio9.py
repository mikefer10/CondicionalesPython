'''
Programa que pide tres números y los muestre ordenados (de mayor a menor)

Entrada:
    numero1 int -> n1
    numero2 int -> n2
    numero3 int -> n3
Salida:
    mensajeRetorno str -> mensaje
'''
n1 = int(input("Número Uno: "))
n2 = int(input("Número Dos: "))
n3 = int(input("Número Tres: "))

if n1 > n2:
    if n1 > n3:
        if n2 > n3:
            print(f"{n1}, {n2}, {n3}")
        else:
            print(f"{n1}, {n3}, {n2}")
    else:
        print(f"{n3}, {n1}, {n2}")
else:
    if n2 > n3:
        if n1 > n3:
            print(f"{n2}, {n1}, {n3}")
        else:
            print(f"{n2}, {n3} , {n1}")
    else:
        print(f"{n3}, {n2}, {n1}")