'''
Juego Piedra Papel y Tijera
Programa que lea las opciones de 2 jugadores, y muestra el resultado
Empate, gana jugador 1 o gana jugador 2
Si introducimos una opción que no coindica con piedra, papel o tijera
Diga que opción Incorrecta

Entrada:
    valorRonda str -> valor
Salida:
    mensajeRetorno str -> men
'''
print("OPCIONES: \nPiedra 🤜 \nPapel 🖐️ \nTijera ✌️")

seguir = 'y'

while seguir == 'y':
    part1 = str(input("Jugador 1 = "))
    part2 = str(input("Jugador 2 = "))

    part1 = part1.lower()
    part2 = part2.lower()
    if part1 == 'piedra':
        if part2 == 'piedra':
            print("Empate")
        elif part2 == 'papel':
            print("Jugador 2 gana")
        elif part2 == 'tijera':
            print("Jugador 1 gana")
        else:
            print("ERROR: Player 2")
    elif part1 == 'papel':
        if part2 == 'piedra':
            print("Jugador 1 gana")
        elif part2 == 'papel':
            print("Empate")
        elif part2 == 'tijera':
            print("Jugador 2 gana")
        else:
            print("ERROR: Player 2")
    elif part1 == 'tijera':
        if part2 == 'piedra':
            print("Jugador 2 gana")
        elif part2 == 'papel':
            print("Jugador 1 gana")
        elif part2 == 'tijera':
            print("Empate")
        else: 
            print("ERROR: Player 2")
    else:
        print("ERROR: Player 1")
    seguir = str(input("¿Deseas Seguir? (y/n): "))
    



