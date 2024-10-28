'''
Programa que pida dos números e indique cuál es el mayor, si son iguales muestre "Son iguales"

Entrada:
    numero1 int -> n1
    numero2 int -> n2
Salida:
    mensajeRetorno str -> mensaje
'''
#Pedimos al usuario que ingrese los dos valores numéricos
n1 = int(input("Ingrsa el primer numero: "))
n2 = int(input("Ingrsa el segundo numero: "))
#Evaluamos cuando es uno mayor, cuando es uno menor y cuando son iguales
if n1>n2:
    print(str(n1)+' es meyor que '+str(n2))
elif n1==n2:
    print(str(n1)+' es igual que '+str(n2))
else:
    print(str(n2)+' es meyor que '+str(n1))
