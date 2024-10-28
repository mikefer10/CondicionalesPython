'''
Programa que pide un nombre de usuario y una contraseña y si se introduce:
"pepe" y "asdasd" se indica "Has entrado al sistema" y si no arroja un error.

Entrada:
    nombreUsuario int -> user
    caracteresContraseña int -> password
Salida:
    mensajeRetorno str -> mensaje
'''
user = str(input("Usuario: "))
password = str(input("Contraseña: "))
if user == 'pepe' and password == 'asdasd':
    print("Has accedido al sistema")
elif user == 'pepe': 
    print("Contraseña incorrecta")
elif password == 'asdasd':
    print("Usuario no encontrado")
else: 
    print("Usuario y contraseña inválidos ")
