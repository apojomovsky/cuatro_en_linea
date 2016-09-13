#!/usr/bin/env python

import unittest
from main import GameBoard
from main import ColumnIsFull
from main import OutOfIndex

class TestGameBoard(unittest.TestCase):
    def test_put_chip(self):
        game = GameBoard()
        game.put_chip(2, 'rojo')
        self.assertEqual(game.read_entry(6, 2), 'rojo')
        game.put_chip(2, 'azul')
        self.assertEqual(game.read_entry(5, 2), 'azul')
        game.put_chip(2, 'azul')
        game.put_chip(2, 'azul')
        game.put_chip(2, 'azul')
        game.put_chip(2, 'azul')
        with self.assertRaises(ColumnIsFull):
            game.put_chip(2, 'amarillo')

    def test_read_entry(self):
        game = GameBoard()
        game.put_chip(1, 'rojo')
        self.assertEqual(game.read_entry(6, 1), 'rojo')
        self.assertEqual(game.read_entry(5, 1), None)
        game.put_chip(1, 'azul')
        self.assertEqual(game.read_entry(5, 1), 'azul')
        with self.assertRaises(OutOfIndex):
          game.read_entry(7, 7)
          game.read_entry(6, 8)


if __name__ == '__main__':
    unittest.main()
