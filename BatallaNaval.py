import time  # Usamos time.sleep() para poder hacer la experiencia más agradable
import random # Usamos random.randint() para poder generar números aleatorios para las posiciones de los barcos
import os  # Usamos os para poder limpiar la consola

# Autores: Eric Gerzenstein, Joaquín García de García Teuly, Eitan Trajtman
# Fecha de entrega: 26/04/24
# Descripción:
# Batalla naval es un juego de mesa en el que dos jugadores compiten por hundir los barcos del oponente.
# Este programa permite jugar al clásico juego de batalla naval en dos modos: de un jugador y de dos jugadores.
# En el modo de un jugador, el jugador trata de adivinar dónde están los barcos puestos por la máquina,
# y tiene un límite de fallos antes de perder.
# El modo de dos jugadores replica el juego de mesa, sin límite de disparos.

while True:
    modo = int(input("¿Qué modo de juego desea jugar? ¿De a 1 (1) o de a 2 (2)? "))

    if modo == 2:
        # ------------------------------ MODO DE DOS JUGADORES ------------------------------
        jugadorUno = input("Jugador 1, ingrese su nombre: ")
        jugadorDos = input("Jugador 2, ingrese su nombre: ")

        N = int(input("Ingresen el tamaño deseado del tablero (número natural): "))
        os.system('cls' if os.name == 'nt' else 'clear')  # A lo largo del código limpia la consola

        contador1:int = 0
        contador2:int = 0

        # Tablero del jugador 1
        tablero: list[list[bool]] = \
            [

            ]

        # Tablero del jugador 2
        tablero2: list[list[bool]] = \
            [

            ]

        os.system('cls' if os.name == 'nt' else 'clear')

        # Crear el tablero para el jugador 1
        for i in range(N):
            fila = [False for x in range(N)]
            tablero.append(fila)

        for fila in tablero:  # Este for, utilizado varias veces a lo largo del código, imprime el tablero en la consola de una forma más lejible
            print(' '.join('_' if not val else str(val) for val in fila))

        # Se asegura que la cantidad de barcos ingresados sea razonable
        while True:
            cantidad_barcos = int(input(f"¿De a cuántos barcos desean jugar (número natural)? "))  # ¿Cuántos barcos quiero ingresar?
            if cantidad_barcos > N:
                print(f"Por favor, ingresen un número menor o igual a {N}")
                print("Prueben de nuevo")
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
            elif cantidad_barcos <= 0:
                print("Deben ingresar un número natural.")
                print("Prueben de nuevo")
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                break

        time.sleep(1)

        if cantidad_barcos == 1:
            print(f"{cantidad_barcos} barco será entonces")
        else:
            print(f"{cantidad_barcos} barcos serán entonces")

        # ------------------------------ SECCIÓN PREPARACIÓN JUGADOR 1 ------------------------------
        print(f"{jugadorUno}, es tu turno")

        time.sleep(1)
        print(3)
        time.sleep(1)
        print(2)
        time.sleep(1)
        print(1)
        time.sleep(1)

        # ¿Dónde los quiero ingresar?
        while contador1 < cantidad_barcos:
            F = int(input(f"Ingrese la fila de su barco (del 1 al {N}): "))
            C = int(input(f"Ingrese la columna de su barco (del 1 al {N}): "))

            if tablero[F - 1][C - 1] == False:
                tablero[F - 1][C - 1] = True
                contador1 += 1
            else:
                print("Ya hay un barco en esa posición")
                time.sleep(1)
            for fila in tablero:
                print(' '.join('X' if val else '_' for val in fila))

        # ------------------------------ SECCIÓN PREPARACIÓN JUGADOR 2 ------------------------------

        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{jugadorDos}, es tu turno")
        time.sleep(3)

        for i in range(N):
            fila = [False for x in range(N)]
            tablero2.append(fila)

        for fila in tablero2:
            print(' '.join('_' if not val else str(val) for val in fila))

        # ¿Dónde los quiero ingresar?
        while contador2 < cantidad_barcos:
            F = int(input(f"Ingrese la fila de su barco (del 1 al {N}): "))
            C = int(input(f"Ingrese la columna de su barco (del 1 al {N}): "))

            if tablero2[F - 1][C - 1] == False:
                tablero2[F - 1][C - 1] = True
                contador2 += 1
            else:
                print("Ya hay un barco en esa posición")
                time.sleep(1)
            for fila in tablero2:
                print(' '.join('X' if val else '_' for val in fila))

        # ------------------------------ SETUP DE JUEGO + LOOP PRINCIPAL ------------------------------

        # Tablero de ataque del jugador 1, replica el tablero del jugador 2
        # pero sin revelar la información de la ubicación de los barcos
        tableroDeAtaque: list[list[bool]] = \
            [

            ]

        for i in range(N):
            fila = [False for x in range(N)]
            tableroDeAtaque.append(fila)

        # Tablero de ataque del jugador 2, replica el tablero del jugador 1
        tableroDeAtaque2: list[list[bool]] = \
            [

            ]

        for i in range(N):
            fila = [False for x in range(N)]
            tableroDeAtaque2.append(fila)

        juegaJugador1 = True
        puntosJugador1:int = 0
        puntosJugador2:int = 0

        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Empieza el juego.")
        time.sleep(3)

        # Loop principal
        while True:
            if juegaJugador1:
                F = int(input(f"{jugadorUno}, ingrese la fila de su ataque (del 1 al {N}): "))
                C = int(input(f"{jugadorUno}, ingrese la columna de su ataque (del 1 al {N}): "))

                if tablero2[F - 1][C - 1] == True:
                    tableroDeAtaque[F - 1][C - 1] = True
                    print("¡Le diste a un barco!")
                    time.sleep(1)
                    puntosJugador1 += 1

                    # Condición de victoria
                    if puntosJugador1 == cantidad_barcos:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(f"¡{jugadorUno} ha ganado!")

                        print(f"Tablero de {jugadorUno}:")
                        time.sleep(1)
                        for fila in tablero:
                            print(' '.join('X' if val else '_' for val in fila))
                        time.sleep(1)

                        print(f"Tablero expuesto de {jugadorDos}:")
                        time.sleep(1)
                        for fila in tablero2:
                            print(' '.join('X' if val else '_' for val in fila))
                        time.sleep(1)

                        break

                    print(f"Tablero expuesto de {jugadorDos}:")
                    time.sleep(1)
                    for i in range(N):
                        # Muestra X, 0 o _ dependiendo de si le diste a un barco, si no le diste a un barco o si no atacaste esa casilla
                        # Se usa para representar el tablero a lo largo del juego
                        print(' '.join(
                            'X' if tableroDeAtaque[i][j] and tablero2[i][j] else 'O' if tableroDeAtaque[i][j] else '_'
                            for j in range(N)))
                    time.sleep(1)

                else:
                    print("¡Fallaste!")
                    time.sleep(1)
                    print(f"La casilla {F}, {C} no tiene un barco")
                    tableroDeAtaque[F - 1][C - 1] = True

                    time.sleep(1)
                    print(f"Tablero de {jugadorDos}:")
                    for i in range(N):
                        print(' '.join(
                            'X' if tableroDeAtaque[i][j] and tablero2[i][j] else 'O' if tableroDeAtaque[i][j] else '_'
                            for j in range(N)))
                juegaJugador1 = False

            else:
                F = int(input(f"{jugadorDos}, ingrese la fila de su ataque (del 1 al {N}): "))
                C = int(input(f"{jugadorDos}, ingrese la columna de su ataque (del 1 al {N}): "))

                if tablero[F - 1][C - 1] == True:
                    tableroDeAtaque2[F - 1][C - 1] = True
                    print("¡Le diste a un barco!")
                    time.sleep(1)
                    puntosJugador2 += 1

                    # Condición de victoria
                    if puntosJugador2 == cantidad_barcos:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(f"¡{jugadorDos} ha ganado!")

                        print(f"Tablero expuesto de {jugadorUno}:")
                        time.sleep(1)
                        for fila in tablero:
                            print(' '.join('X' if val else '_' for val in fila))
                        time.sleep(1)

                        print(f"Tablero expuesto de {jugadorDos}:")
                        time.sleep(1)
                        for fila in tablero2:
                            print(' '.join('X' if val else '_' for val in fila))
                        time.sleep(1)

                        break

                    print(f"Tablero de {jugadorUno}:")
                    time.sleep(1)
                    for i in range(N):
                        print(' '.join(
                            'X' if tableroDeAtaque2[i][j] and tablero[i][j] else 'O' if tableroDeAtaque2[i][j] else '_'
                            for j in range(N)))
                    time.sleep(1)

                else:
                    print("¡Fallaste!")
                    time.sleep(1)
                    print(f"La casilla {F}, {C} no tiene un barco")
                    tableroDeAtaque2[F - 1][C - 1] = True

                    f"Tablero de {jugadorUno}:"
                    time.sleep(1)
                    for i in range(N):
                        print(' '.join(
                            'X' if tableroDeAtaque2[i][j] and tablero[i][j] else 'O' if tableroDeAtaque2[i][j] else '_'
                            for j in range(N)))
                juegaJugador1 = True

    elif modo == 1:
        jugador = input("Ingrese su nombre: ")
        N = int(input("Ingrese el tamaño deseado del tablero (número natural)"))

        tablero: list[list[bool]] = \
            [

            ]

        for i in range(N):
            fila = [False for x in range(N)]
            tablero.append(fila)

        for fila in tablero:
            print(' '.join('_' if not val else str(val) for val in fila))

        while True:
            cantidad_barcos = int(input(f"¿De a cuántos barcos desea jugar (número natural)? "))
            if cantidad_barcos > N:
                print(f"Por favor, ingrese un número menor o igual a {N}")
                print("Pruebe de nuevo")
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
            elif cantidad_barcos <= 0:
                print("Debe ingresar un número natural.")
                print("Pruebe de nuevo")
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                break

        time.sleep(1)
        print(f"Habrán {cantidad_barcos} barcos en el tablero, los cuales pueden ocupar entre 1 a 3 casillas.")
        contador = 0

        espacios_totales = 0
        # Ubicación autónoma de los barcos
        while contador < cantidad_barcos:
            F = random.randint(1, N - 1)
            C = random.randint(1, N - 1)
            S = random.randint(1, 3)
            D = random.randint(0, 1)

            if tablero[F - 1][C - 1] == False:
                # Posicionamiento de barcos horizontalmente
                if D == 0:
                    if C + S - 1 <= N:
                        for i in range(S):
                            tablero[F - 1][C - 1 + i] = True
                        contador += 1
                        espacios_totales += S
                # Posicionamiento de barcos verticalmente
                else:
                    if F + S - 1 <= N:
                        for i in range(S):
                            tablero[F - 1 + i][C - 1] = True
                        contador += 1
                        espacios_totales += S

        tableroDeAtaque: list[list[bool]] = \
            [

            ]

        for i in range(N):
            fila = [False for x in range(N)]
            tableroDeAtaque.append(fila)

        print(f"Prepárate para jugar, {jugador}.")
        time.sleep(1)
        print(f"Tendrás un máximo de {3 * N} disparos para hundir todos los barcos.")
        print(3)
        time.sleep(1)
        print(2)
        time.sleep(1)
        print(1)
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')

        puntos = 0
        disparos = 0
        limit = 3 * N

        while True:
            F = int(input(f"{jugador}, ingrese la fila de su ataque (del 1 al {N}): "))
            C = int(input(f"{jugador}, ingrese la columna de su ataque (del 1 al {N}): "))

            if tablero[F - 1][C - 1] == True:
                tableroDeAtaque[F - 1][C - 1] = True
                print("¡Le diste a un barco!")
                time.sleep(1)
                puntos += 1

                # Condición de victoria
                if puntos == espacios_totales:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f"Has ganado, {jugador}!")

                    print(f"Tablero:")
                    time.sleep(1)
                    for fila in tablero:
                        print(' '.join('X' if val else '_' for val in fila))
                    time.sleep(1)

                    break

                print(f"Tablero:")
                time.sleep(1)
                for i in range(N):
                    print(' '.join(
                        'X' if tableroDeAtaque[i][j] and tablero[i][j] else 'O' if tableroDeAtaque[i][j] else '_'
                        for j in range(N)))
                time.sleep(1)

            else:
                print("¡Fallaste!")
                time.sleep(1)
                print(f"La casilla {F}, {C} no tiene un barco")
                tableroDeAtaque[F - 1][C - 1] = True
                disparos += 1

                # Condición de derrota
                if disparos == limit:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f"Has perdido, {jugador}.")

                    print(f"Tablero:")
                    time.sleep(1)
                    for fila in tablero:
                        print(' '.join('X' if val else '_' for val in fila))
                    time.sleep(1)

                    break

                time.sleep(1)
                print(f"Tablero:")
                for i in range(N):
                    print(' '.join(
                        'X' if tableroDeAtaque[i][j] and tablero[i][j] else 'O' if tableroDeAtaque[i][j] else '_'
                        for j in range(N)))

    else:
        print("Por favor, ingrese '1' o '2'")
