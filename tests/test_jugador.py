import unittest #Libreria que investigue y la aplique, sirve para pruebas unitarias en python
from game.tablero import Tablero
from game.jugador import Jugador

class TestJugador(unittest.TestCase):
    def setUp(self):
        self.tablero = Tablero()
        self.jugador = Jugador("TestPlayer")
        
    def test_mover_normal(self):
        #test normal
        self.jugador.mover(3, self.tablero)
        self.assertEqual(self.jugador.posicion, 4)

    def test_mover_ganar(self):
        #test 100 y ganar
        self.jugador.posicion = 97
        self.jugador.mover(3, self.tablero)
        self.assertEqual(self.jugador.posicion, 100)

    def test_mover_superar_100(self):
        #test que no pase de 100
        self.jugador.posicion = 97
        self.assertFalse(self.jugador.mover(4, self.tablero))
        self.assertEqual(self.jugador.posicion, 97)

if __name__ == '__main__':
    unittest.main()

