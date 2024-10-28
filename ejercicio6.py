'''
Programa que lee una cadena y compruebe si es una letra mayúscula.

Entrada:
    cadenaCaracteres int -> c
Salida:
    mensajeRetorno str -> mensaje
'''
c = str(input("Introduce una letra: "))
may = c.isupper()
if may == True and len(c) == 1:
    print(c, " -> es mayuscula")
elif len(c) > 1:
    print("Ingresa solo una letra")
else:
    print(c, " -> es minúscula")