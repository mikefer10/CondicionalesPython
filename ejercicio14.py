'''
Escribe un programa que pida un número entero entre uno y doce e imprima el 
número de días que tiene el mes correspondiente.
Si introducimos otro número nos da un error.

Entrada:
    numeroMes int -> mes
Salida:
    mensajeRetorno str -> dias_en_mes
'''
'''
Esta función se basa de un diccionario que contiene de los días que tienen los 12 meses del
año, primero evalúa si el número ingresado está entre el rango de (1-12), si no se cumple 
devuelve "0", si se cumple retorna los días que tiene ese mes (valor asociado).
'''
def dias_en_mes(mes):
    # Diccionario con la cantidad de días para cada mes
    dias_por_mes = {
        1: 31,  # Enero
        2: 28,  # Febrero
        3: 31,  # Marzo
        4: 30,  # Abril
        5: 31,  # Mayo
        6: 30,  # Junio
        7: 31,  # Julio
        8: 31,  # Agosto
        9: 30,  # Septiembre
        10: 31, # Octubre
        11: 30, # Noviembre
        12: 31  # Diciembre
    }
    #Verifica si el valor del mes está entre  1 y 12
    if mes in dias_por_mes:
        return dias_por_mes[mes]
    else:
        return 0

'''
Aquí creamos otra función que lo que hace es que al recibir el valor numérico del mes va a 
evaluar si coincide con alguna clave o llave en el diccionero que contiene el equivalente del 
mes en letras si no hay ninguna conicidencia solo devuelve un "0" como valor simbólico
'''    
def mes_letras(mes):
    #Diccionario que asocia los meses en número con los meses en letras 
    meses = {
        1: "Enero",
        2: "Febrero",
        3: "Marzo", 
        4: "Abril", 
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto",
        9: "Septiembre", 
        10: "Octubre",
        11: "Noviembre",
        12: "Diciembre"
    }
    #Verifica si el valor del mes coincide con las claves del diccionerio (entre  1 y 12)
    if mes in meses:
        return meses[mes]
    else:
        return 0

#Aquí solicitamos que el usuario ingrese un valor numérico entre 1 y 12
try: #Esto indica que es lo que se espera recibir, en este caso un valor (type: int)
    valor_mes = int(input("Ingrese un número entero entre 1 y 12: "))
    dias_mes = dias_en_mes(valor_mes)
    mes = mes_letras(valor_mes)
    if valor_mes >= 1 and valor_mes <= 12:
        print(f"{mes} tiene {dias_mes} días")
    elif dias_en_mes(mes) == 0 or mes_letras(mes) == 0:
        print("Error: El mes no existe")
except ValueError: #Esto indica que si no se recibe lo que se espera ejecuta otra cosa (Error)
    print("Error: Entrada no válida")