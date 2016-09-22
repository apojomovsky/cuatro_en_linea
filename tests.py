#!/usr/bin/env python

import unittest
import numpy as np
from gameboard import GameBoard
from gameboard import ColumnIsFull
from gameboard import OutOfIndex


class TestGameBoard(unittest.TestCase):

    def setUp(self):
        self.game = GameBoard()
        self.reference_matrix = np.array([['-', '-', '-', '-', '-', '-', '-'],
                                          ['blue', '-', '-', '-', '-', '-', '-'],
                                          ['red', '-', 'red', '-', '-', '-', '-'],
                                          ['blue', 'blue', 'red', 'red', '-', '-', '-'],
                                          ['red', 'red', 'red', 'blue', '-', '-', '-'],
                                          ['red', 'blue', 'blue', 'blue', '-', '-', '-']], dtype='a5')

    def test_put_chip(self):
        self.game.put_chip(3, 'red')
        self.assertEqual(self.game.matrix[:, 2][5], 'red')
        self.game.put_chip(3, 'blue')
        self.assertEqual(self.game.matrix[:, 2][4], 'blue')
        self.game.matrix = self.reference_matrix
        self.game.put_chip(1, 'red')
        with self.assertRaises(ColumnIsFull):
            self.game.put_chip(1, 'red')

    def test_read_entry(self):
        self.game.matrix = self.reference_matrix
        self.assertEqual(self.game.read_entry(1, 1), 'red')
        self.assertEqual(self.game.read_entry(2, 1), 'red')
        self.assertEqual(self.game.read_entry(1, 2), 'blue')
        with self.assertRaises(OutOfIndex):
            self.game.read_entry(7, 1)
        with self.assertRaises(OutOfIndex):
            self.game.read_entry(1, 8)

    def test_check_rows(self):
        self.game.matrix = self.reference_matrix
        self.assertEqual(self.game.check_rows(), False)
        self.game.matrix[:, 4][5] = 'blue'
        self.assertEqual(self.game.check_rows(), True)

    def test_check_columns(self):
        self.game.matrix = self.reference_matrix
        self.assertEqual(self.game.check_columns(), False)
        self.game.matrix[:, 2][1] = 'red'
        self.assertEqual(self.game.check_columns(), True)

    def test_check_diagonals(self):
        self.game.matrix = self.reference_matrix
        self.assertEqual(self.game.check_diagonals(), False)
        self.game.matrix[:, 3][2] = 'red'
        self.assertEqual(self.game.check_diagonals(), True)

if __name__ == '__main__':
    unittest.main()
