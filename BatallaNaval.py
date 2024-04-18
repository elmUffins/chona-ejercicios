import time

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
time.sleep(3)

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
    for fila in tablero2:
        print(' '.join('B' if val else 'X' for val in fila))

