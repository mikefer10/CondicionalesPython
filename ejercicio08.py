'''
Programa que pide dos números 'nota' y 'edad' y un carácter 'sexo' y muestre 'ACEPTADA' si:
1. Nota es mayor o igual a cinco 
2. Edad es mayor o igual a dieciocho 
3. Sexo es 'F' 
En caso de que se cumpla lo mismo, pero el sexo sea 'M', debe imprimir 'POSIBLE'. 
Si no se cumplen dichas condiciones se debe mostrar 'NO ACEPTADA'.

Entrada:
    notaUsuario int -> nota
    edadUsuario int -> edad
    caracterSexo str -> sexo
Salida:
    mensajeRetorno str -> mensaje
'''
sexo = str(input("¿Cuál es tu sexo? (F/M): "))
edad = int(input("Ingrsa tu edad: "))
nota = int(input("Ingresa tu nota "))

if nota >= 5 and edad >= 18 and sexo == 'F':
    print("ACEPTADA")
elif nota >= 5 and edad >= 18 and sexo == 'M':
    print("POSIBLE")
elif sexo != 'F' and sexo != 'M':
    print("¡Sexo no acepdato!")
else:
    print("NO ACEPTADA")