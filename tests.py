#!/usr/bin/env python

import unittest
from gameboard import GameBoard
from gameboard import ColumnIsFull
from gameboard import OutOfIndex

class TestGameBoard(unittest.TestCase):

    def test_put_chip(self):
        game = GameBoard()
        # test if red chip is put at the bottom of the column
        game.put_chip(2, 'red')
        self.assertEqual(game.read_entry(1, 2), 'red')

        # test if blue chip is put above the red one
        game.put_chip(2, 'blue')
        self.assertEqual(game.read_entry(2, 2), 'blue')

        # fill the column with blue chips
        game.put_chip(2, 'blue')
        game.put_chip(2, 'blue')
        game.put_chip(2, 'blue')
        game.put_chip(2, 'blue')

        # test if column is full
        with self.assertRaises(ColumnIsFull):
            game.put_chip(2, 'yellow')

    def test_read_entry(self):
        game = GameBoard()

        # put a red chip into column 1 and test if true
        game.put_chip(1, 'red')
        self.assertEqual(game.read_entry(1, 1), 'red')

        # test that there is an empty cell above the red one
        self.assertEqual(game.read_entry(2, 1), '-')

        # put a blue chipe above the red and test if true
        game.put_chip(1, 'blue')
        self.assertEqual(game.read_entry(2, 1), 'blue')

        # test invalid entries to raise an error
        with self.assertRaises(OutOfIndex):
          game.read_entry(7, 7)
          game.read_entry(6, 8)


if __name__ == '__main__':
    unittest.main()
