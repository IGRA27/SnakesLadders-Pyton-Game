from game.tablero import Tablero
from game.jugador import Jugador
from game.dado import lanzar_dado

def jugar():
    tablero = Tablero()
    jugador1 = Jugador("Jugador 1")
    jugador2 = Jugador("Jugador 2")
    jugadores = [jugador1, jugador2]

    while True:
        for jugador in jugadores:
            input(f"{jugador.nombre}, presiona 'Enter' para lanzar el dado")
            valor_dado = lanzar_dado()
            jugador.mover(valor_dado, tablero)
            print(f"{jugador.nombre} ha lanzado un {valor_dado} y se mueve a la casilla {jugador.posicion}")
            if jugador.posicion == 100:
                print(f"¡Felicidades futuro pasante BAYTEQ {jugador.nombre}, ENHORABUENA HAS GANADO EL JUEGO!")
                return

if __name__ == "__main__":
    jugar()
