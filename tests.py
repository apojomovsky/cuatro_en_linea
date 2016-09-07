import unittest
from main import Tablero
from main import ColumnIsFull

class TestTablero(unittest.TestCase):
    def test_put_chip(self):
        tablero = Tablero(2,2)
        tablero.put_chip(2, 'rojo')
        self.assertEqual(tablero.read_entry(2, 2), 'rojo')
        tablero.put_chip(2, 'azul')
        self.assertEqual(tablero.read_entry(1, 2), 'azul')
        with self.assertRaises(ColumnIsFull):
            tablero.put_chip(2, 'amarillo')

if __name__ == '__main__':
    unittest.main()
