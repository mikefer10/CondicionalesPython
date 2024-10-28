'''
Pide el día de la semana (del 1 al 7) y escriba el día correspondiente. 
Si introducimos otro número nos da un error.

Entrada:
    diaSemana int -> dia_num
Salida:
    diaSemanaLetra str -> dia_letra
'''
dia_num = int(input("¿Qué día de la semana es?: "))
def dia_semana_letra(numero):
    caras_opuestas = {
        1: "Lunes",
        2: "Martes",
        3: "Miércoles",
        4: "Jueves",
        5: "Viernes",
        6: "Sábado",
        7: "Domingo"
    }
    if 1 <= numero <= 7:
        return caras_opuestas[numero]
    else:
        return False

if dia_semana_letra(dia_num) == False:
    if dia_num > 7:
        print(f"¡No existen semanas de {dia_num} días!")
    elif dia_num < 1:
        print("↺ Inténtalo más tarde")
else:
    print(f"El día {dia_num} de la semana es {dia_semana_letra(dia_num)}")