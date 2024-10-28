'''
Programa que pide al usuario dos números y muestre su división 
si el segundo no es cero, o un mensaje de aviso en caso contrario.

Entrada:
    numero int -> num
Salida:
    mensajeRetorno str -> mensaje
'''
div1 = int(input("Introduce el divisor: "))
div2 = int(input("Introduce el dividendo: "))
if div2 == 0:
    print("Rescuerda que no es posible dividir entre 0")
else:
    res = div1 / div2
    res_red = f"{res:.1f}"
    print(str(div1)+" ÷ "+str(div2)+" = "+str(res_red))
