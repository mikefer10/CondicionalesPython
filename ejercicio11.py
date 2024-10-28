'''
La política de cobro de una compañía telefónica es: cuando se realiza una llamada, 
el cobro es por el tiempo que ésta dura, de tal forma que los primeros cinco minutos 
cuestan 1 euro, los siguientes tres, 80 céntimos, los siguientes dos minutos, 70 céntimos,
y a partir del décimo minuto, 50 céntimos. Además, se carga un impuesto de 3 % cuando es 
domingo, y si es otro día, en turno de mañana, 15 %, y en turno de tarde, 10 %. 
Realice un programa para determinar cuánto debe pagar por cada concepto 
una persona que realiza una llamada.

Entrada:
    timpoServicio int -> tiempo
    diaLlamada str -> dia
    horarioUso -> hora
Salida:
    pagaServivio int -> paga
'''
#Esta función recibe como parámetro el tiempo para calcular el costo de la llamada sin comisiones 
def calcular_costo_base(tiempo):
    if tiempo <= 5:
        return tiempo * 1
    elif tiempo <= 8:
        return 5 + (tiempo - 5) * 0.80
    elif tiempo <= 10:
        return 7.4 + (tiempo - 8) * 0.70
    else:
        return 8.8 + (tiempo - 10) * 0.50
'''
En esta función se reciben como parámetros el costo hasta el momento, el día y
horario de la llamada para determinar el costo únicamente de la comisión.
''' 
def calcular_impuesto(pago, dia, hora):
    dia = dia.lower()
    if dia == 'domingo':
        return pago * 0.03
    elif dia in ['lunes', 'martes', 'miércoles', 'miercoles', 'jueves', 'viernes', 'sábado', 'sabado']:
        if hora < 12:
            return pago * 0.15
        else:
            return pago * 0.10
    else:
        print("Día de la semana inválido :(")
        return 0  #Como ya no se va a efectuar una operación no se espera que retorne ningún valor

#Aquí pedimos por teclado que el usuario ingrese los datos que necesitamos (tiempo, dia, hora)
tiempo = int(input("Minutos que duró la llamada: "))
dia = input("Día que se realizó la llamada: ")
hora = int(input("Horario de 00:00 Hrs a 24:00 Hrs en que se efectuó: "))

'''
Aquí mandamos a llamar las funciones declaradas antes y colocamos como 
parámetros las veriables necasarias y así efectuar las operaciones 
'''
pago_base = calcular_costo_base(tiempo)
impuesto = calcular_impuesto(pago_base, dia, hora)

#Como una función calcula en costo sin impuesto y la otra el impuesto sumamos ambos resultados
total_pago = pago_base + impuesto

print(f"◇ El costo de la llamada es de ${pago_base:.2f} pero se te cobrará una comisión adicional de ${impuesto:.2f}")
#Por último imprimimos por consola lo que debe pagar el usuario
print(f"✓ EN TOTAL DEBES PAGAR ${total_pago:.2f}")