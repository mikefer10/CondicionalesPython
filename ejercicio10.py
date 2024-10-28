'''
El director de una escuela está organizando un viaje de estudios, y requiere 
determinar cuánto debe cobrar a cada alumno y cuánto debe pagar a la compañía de 
viajes por el servicio. La forma de cobrar es la siguiente: 
si son 100 alumnos o más, el costo por cada alumno es de 65 euros; 
de 50 a 99 alumnos, el costo es de 70 euros, de 30 a 49, de 95 euros, 
y si son menos de 30, el costo de la renta del autobús es de 4000 euros, 
sin importar el número de alumnos. 
Realice un programa que permita determinar el pago a la compañía de autobuses 
y lo que debe pagar cada alumno por el viaje.

Entrada:
    numeroAlumnos int -> n_a
Salida:
    mensajeRetorno str -> mensaje
'''
n_a = int(input("Alumnos que asistirán: "))
if n_a >= 100:
    pagar = n_a * 65
    print("$65 por alumno para cubrir los $"+str(pagar)+" del autobús")
elif n_a >= 50 and n_a <= 99:
    pagar= n_a * 70
    print("$70 por alumno para cubrir los $"+str(pagar)+" del autobús")
elif n_a >= 30 and n_a <= 49:
    pagar = n_a * 95
    print("$95 por alumno para cubrir los $"+str(pagar)+" del autobús")
elif n_a > 0 and n_a <= 29:
    pagar = n_a * (4000/n_a)
    p_a = 4000/n_a
    p_a_red = f"{p_a:.0f}"
    pagar_red = f"{pagar:.0f}"
    print(f"{p_a_red} por alumno para cubrir los $"+str(pagar_red)+" del autobús")