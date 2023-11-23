import unittest  #Libreria que investigue y la aplique, sirve para pruebas unitarias en python
from game.dado import lanzar_dado

class TestDado(unittest.TestCase):
    def test_lanzar_dado(self):
        resultado = lanzar_dado()
        self.assertTrue(1 <= resultado <= 6, "El resultado debe estar entre 1 y 6")

if __name__ == '__main__':
    unittest.main()
