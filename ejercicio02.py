'''
Programa que pida un número y diga si es positivo, negativo o 0.

Entrada:
    numero int -> num
Salida:
    mensajeRetorno str -> mensaje
'''
num = int(input("Ingrsa un número positivo o negativo: "))
if num > 0:
    print(str(num)+" es positivo")
elif num == 0:
    print(str(num)+" es igual a cero")
else:
    print(str(num)+" es negativo")