#Libreria que investigue y la aplique, sirve para pruebas unitarias en python
import unittest
from game.tablero import Tablero

class TestTablero(unittest.TestCase):
    def setUp(self):
        self.tablero = Tablero()

    def test_verificar_casilla(self):
        #prueba
        self.assertEqual(self.tablero.verificar_casilla(4), 4, "Debería quedarse en la misma casilla si no hay serpiente ni escalera")
        #Prueba
        self.assertEqual(self.tablero.verificar_casilla(2), 38, "Debería subir por la escalera")
        #prueba
        self.assertEqual(self.tablero.verificar_casilla(16), 6, "Debería bajar por la serpiente")

if __name__ == '__main__':
    unittest.main()

