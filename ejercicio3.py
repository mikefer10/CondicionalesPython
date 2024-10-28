'''
Programa que lee un número e imprime si es par o impar.

Entrada:
    numero int -> num
Salida:
    mensajeRetorno str -> mensaje
'''
num = int(input("Ingrsa un número entero: "))
if num % 2 == 0:
    print(str(num)+" es un número par")
else:
    print(str(num)+" es un número impar")