# Juego de Piedra, Papel o Tijera para dos jugadores

def obtener_eleccion(jugador):
    while True:
        eleccion = input(f"Jugador {jugador}, elige Piedra, Papel o Tijera: ").strip().lower()
        if eleccion in ["piedra", "papel", "tijera"]:
            return eleccion
        else:
            print("Elección inválida. Por favor elige entre Piedra, Papel o Tijera.")

def determinar_ganador(eleccion1, eleccion2):
    if eleccion1 == eleccion2:
        return "¡Es un empate!"
    elif (eleccion1 == "piedra" and eleccion2 == "tijera") or \
         (eleccion1 == "papel" and eleccion2 == "piedra") or \
         (eleccion1 == "tijera" and eleccion2 == "papel"):
        return "¡Jugador 1 gana!"
    else:
        return "¡Jugador 2 gana!"

# Obtener elecciones de los jugadores
eleccion_jugador1 = obtener_eleccion(1)
eleccion_jugador2 = obtener_eleccion(2)

# Determinar y mostrar el ganador
resultado = determinar_ganador(eleccion_jugador1, eleccion_jugador2)
print(resultado)
