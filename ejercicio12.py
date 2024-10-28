'''
Realiza un programa que pida por teclado el resultado (dato entero) obtenido 
al lanzar un dado de seis caras y muestre por pantalla el número en letras 
(dato cadena) de la cara opuesta al resultado obtenido.
* Nota 1: En las caras opuestas de un dado de seis caras están los números: 
1-6, 2-5 y 3-4.
* Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6, 
se mostrará el mensaje: "ERROR: número incorrecto.".

Entrada:
    numeroRecibido int -> num
Salida:
    caraOpuesta str -> opuesto
    caraObtenida str -> obtenido
'''
'''
Esta es una función que permite asociar los números 1,2,3,4,5,6 a sus equivalentes en 
letras mediante el uso de un diccionario, en este caso los números son las llaves o claves
que nos permite acceder al valor asociado que en este caso son los números ecritos en letras,
recibimos como parámetro el número leído por consola y lo comparamos si es que coincide con una
clave y retornamos el valor asociado, si no coincide solo se devuelve un "0", es algo simbólico 
'''
def cara_opuesta_dado(num):
    caras_opuestas = {
        1: "Seis",
        2: "Cinco",
        3: "Cuatro",
        4: "Tres",
        5: "Dos",
        6: "Uno"
    }
    if 1 <= num <= 6:
        return caras_opuestas[num]
    else:
        return 0

'''
Esta función es similar a la anterior, recibe como parámetro el número leído por teclado para que
haga una comparación en el diccionario, pero en este caso no relacionamos el valor numérico con
su opuesto en letras, sino que es su verdadero equivalente en letras, comparamos nuevamente si
es que cumple con las condiciones (que sea un número entre 1 y 6), si no lo es, devuleve un "0"
'''
def cara_obtenida_dado(num):
    caras_obtenidas = {
        1: "Uno",
        2: "Dos",
        3: "Tres",
        4: "Cuatro",
        5: "Cinco",
        6: "Seis"
    }
    if 1 <= num <= 6:
        return caras_obtenidas[num]
    else:
        return 0
    
#En esta parte le pedimos al usuario que ingrese el número de caras que obtuvo al lanzar el dado
num = int(input("Cara del dado obtenida en el lanzamiento: "))
#Aquí mandamos a llamar a las funciones, y enviamos con los parámetros necesarios "num" 
opuesto = cara_opuesta_dado(num)
obtenido = cara_obtenida_dado(num)
'''
Como el usuario puede ingresar otros números, se puede esperar un 0 en cada una de las funciones 
hacemos una condición que se debe cumplir y es básicamente la misma: (si en número es menor a 1 o 
mayor a 6 entonces arrojará un mensaje de error, si no solo imprime lo que cada función retornó)
'''
if opuesto == 0 or obtenido == 0:
    print("ERROR: número incorrecto.")
else:
    print(f"La cara opuesta de {obtenido} es {opuesto}")