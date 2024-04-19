import time

# Autores: Eric Gerzenstein, Joaquín García de García Teuly, Eitan Trajtman
# Fecha de entrega: 26/04/24
# Descripción: Batalla naval

jugadorUno = input("Jugador 1, ingrese su nombre: ")
jugadorDos = input("Jugador 2, ingrese su nombre: ")

N = int(input("Ingresen el tamaño deseado del tablero: "))
contador1 = 0
contador2 = 0

#Tablero del jugador 1
tablero: list[list[bool]] = \
    [

    ]

#Tablero del jugador 2
tablero2: list[list[bool]] = \
    [

    ]

# ------------------------------ SECCIÓN PREPARACIÓN JUGADOR 1 ------------------------------

print(f"{jugadorUno}, es tu turno")
time.sleep(1)
print(3)
time.sleep(1)
print(2)
time.sleep(1)
print(1)
time.sleep(1)


#Crear el tablero para el jugador 1
for i in range(N):
    fila = [False for x in range(N)]
    tablero.append(fila)

for fila in tablero: #Este for, utilizado varias veces a lo largo del código, imprime el tablero en la consola de una forma más lejible
    print(' '.join('X' if not val else str(val) for val in fila))

cantidad_barcos = int(input(f"¿De a cuántos barcos desean jugar? ")) #¿Cuántos barcos quiero ingresar?

#¿Dónde los quiero ingresar?
while contador1 < cantidad_barcos:
    F = int(input("Ingrese la fila de su barco: "))
    C = int(input("Ingrese la columna de su barco: "))

    if tablero[F - 1][C - 1] == False:
        tablero[F - 1][C - 1] = True
        contador1 += 1
    else:
        print("Ya hay un barco en esa posición")
        time.sleep(1)
    for fila in tablero:
        print(' '.join('B' if val else 'X' for val in fila))

# ------------------------------ SECCIÓN PREPARACIÓN JUGADOR 2 ------------------------------

print(f"{jugadorDos}, es tu turno")
time.sleep(3)

for i in range(N):
    fila = [False for x in range(N)]
    tablero2.append(fila)

for fila in tablero2:
    print(' '.join('X' if not val else str(val) for val in fila))

#¿Dónde los quiero ingresar?
while contador2 < cantidad_barcos:
    F = int(input("Ingrese la fila de su barco: "))
    C = int(input("Ingrese la columna de su barco: "))

    if tablero2[F - 1][C - 1] == False:
        tablero2[F - 1][C - 1] = True
        contador2 += 1
    else:
        print("Ya hay un barco en esa posición")
        time.sleep(1)
    for fila in tablero2:
        print(' '.join('B' if val else 'X' for val in fila))

# ------------------------------ SETUP DE JUEGO + LOOP PRINCIPAL ------------------------------

#Tablero de ataque del jugador 1, replica el tablero del jugador 2
# pero sin revelar la información de la ubicación de los barcos
tableroDeAtaque: list[list[bool]] = \
    [

    ]

for i in range(N):
    fila = [False for x in range(N)]
    tableroDeAtaque.append(fila)

#Tablero de ataque del jugador 2, replica el tablero del jugador 1
tableroDeAtaque2: list[list[bool]] = \
    [

    ]

for i in range(N):
    fila = [False for x in range(N)]
    tableroDeAtaque2.append(fila)

juegaJugador1 = True
puntosJugador1 = 0
puntosJugador2 = 0

time.sleep(1)
print("Empieza el juego.")
time.sleep(3)

#Loop principal
while True:
    if juegaJugador1:
        F = int(input(f"{jugadorUno}, ingrese la fila de su ataque: "))
        C = int(input(f"{jugadorUno}, ingrese la columna de su ataque: "))

        if tablero2[F - 1][C - 1] == True:
            tableroDeAtaque[F - 1][C - 1] = True
            print("¡Le diste a un barco!")
            time.sleep(1)
            puntosJugador1 += 1

            #Condición de victoria
            if puntosJugador1 == cantidad_barcos:
                print(f"¡{jugadorUno} ha ganado!")
                break

            print(f"Tablero de {jugadorDos}:")
            time.sleep(1)
            for i in range(N):
                #Muestra B, 0 o X dependiendo de si le diste a un barco, si no le diste a un barco o si no atacaste esa casilla
                #Se usa para representar el tablero a lo largo del juego
                print(' '.join('B' if tableroDeAtaque[i][j] and tablero2[i][j] else 'O' if tableroDeAtaque[i][j] else 'X' for j in range(N)))
            time.sleep(1)

        else:
            print("¡Fallaste!")
            time.sleep(1)
            print(f"La casilla {F}, {C} no tiene un barco")
            tableroDeAtaque[F - 1][C - 1] = True

            time.sleep(1)
            for i in range(N):
                print(' '.join('B' if tableroDeAtaque[i][j] and tablero2[i][j] else 'O' if tableroDeAtaque[i][j] else 'X' for j in range(N)))
        juegaJugador1 = False

    else:
        F = int(input(f"{jugadorDos}, ingrese la fila de su ataque: "))
        C = int(input(f"{jugadorDos}, ingrese la columna de su ataque: "))

        if tablero[F - 1][C - 1] == True:
            tableroDeAtaque2[F - 1][C - 1] = True
            print("¡Le diste a un barco!")
            time.sleep(1)
            puntosJugador2 += 1

            #Condición de victoria
            if puntosJugador2 == cantidad_barcos:
                print(f"¡{jugadorDos} ha ganado!")
                break

            print(f"Tablero de {jugadorUno}:")
            time.sleep(1)
            for i in range(N):
                print(' '.join('B' if tableroDeAtaque2[i][j] and tablero[i][j] else 'O' if tableroDeAtaque2[i][j] else 'X' for j in range(N)))
            time.sleep(1)

        else:
            print("¡Fallaste!")
            time.sleep(1)
            print(f"La casilla {F}, {C} no tiene un barco")
            tableroDeAtaque2[F - 1][C - 1] = True
            time.sleep(1)
            for i in range(N):
                print(' '.join('B' if tableroDeAtaque2[i][j] and tablero[i][j] else 'O' if tableroDeAtaque2[i][j] else 'X' for j in range(N)))
        juegaJugador1 = True
