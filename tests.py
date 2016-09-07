import unittest
from main import Tablero

class TestTablero(unittest.TestCase):
    def test_gameboard_creation(self):
        tablero = Tablero(2,2)
        tablero.put_chip(2, 'rojo')
        self.assertEqual(tablero.read_entry(2, 2), 'rojo')

if __name__ == '__main__':
    unittest.main()
