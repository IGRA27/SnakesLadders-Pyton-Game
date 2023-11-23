class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.posicion = 1

    def mover(self, valor_dado, tablero):
        nueva_posicion = self.posicion + valor_dado
        if nueva_posicion > 100:  #Jugador no se mueve si supera 100, aunque no deberia pasar en la vida real, pero es para las pruebas, se aplica en Agile Metodologias
            print(f"{self.nombre} lanza {valor_dado} pero se queda en la casilla {self.posicion} porque superaría 100.")
            return False
        #Muevo al jugador y verifico si hay serpientes o escaleras
        self.posicion = tablero.verificar_casilla(nueva_posicion)
        print(f"{self.nombre} lanza {valor_dado} y se mueve a la casilla {self.posicion}")
        return True
