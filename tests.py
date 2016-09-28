#!/usr/bin/env python

import unittest
import numpy
from gameboard import GameBoard
from gameboard import ColumnIsFull
from gameboard import OutOfIndex
from match import Match


class TestGameBoard(unittest.TestCase):

    def setUp(self):
        self.game = GameBoard()

        self.rows_on_corners_matrix = numpy.array([
                    ['-',    'red',  'red',  'red',   '-',   '-', '-'],
                    ['red', 'blue',  'red', 'blue',   '-',   '-', '-'],
                    ['blue', 'red', 'blue',  'red',   '-',   '-', '-'],
                    ['blue', 'red',  'red', 'blue',   '-',   '-', '-'],
                    ['red', 'blue',  'red', 'blue',   '-',   '-', '-'],
                    ['blue', 'red', 'blue',  'red', 'red', 'red', '-']], dtype='a5')

        self.columns_on_corners_matrix = numpy.array([
                    ['-',    '-', '-', '-', '-', '-',    '-'],
                    ['blue', '-', '-', '-', '-', '-', 'blue'],
                    ['blue', '-', '-', '-', '-', '-', 'blue'],
                    ['blue', '-', '-', '-', '-', '-', 'blue'],
                    ['red',  '-', '-', '-', '-', '-',  'red'],
                    ['red',  '-', '-', '-', '-', '-',  'red']], dtype='a5')

        self.diagonals_on_corners_matrix = numpy.array([
                    ['-',       '-',    '-',    '-',    '-',    '-',    '-'],
                    ['red',   'red',    '-',    '-',    '-',  'red', 'blue'],
                    ['blue', 'blue',  'red',    '-',  'red', 'blue',  'red'],
                    ['red',  'blue',  'red',  'red',  'red', 'blue', 'blue'],
                    ['blue',  'red', 'blue', 'blue', 'blue',  'red',  'red'],
                    ['red',  'blue', 'blue',  'red', 'blue',  'red', 'blue']], dtype='a5')

        self.invalid_matrix = numpy.array([
                    ['yellow',  '-',    '-',    '-',    '-',    '-',    '-'],
                    ['red',   'red',    '-',    '-',    '-',  'red',    '-'],
                    ['blue', 'blue',  'red',    '-',  'red', 'blue',    '-'],
                    ['red',  'blue',  'red',  'red',  'red', 'blue', 'blue'],
                    ['blue',  'red', 'blue', 'blue', 'blue',  'red',  'red'],
                    ['red',  'blue', 'blue',  'red', 'blue',  'red', 'blue']], dtype='a5')


    def test_put_chip(self):
        self.game.put_chip(3, 'red')
        self.assertEqual(self.game.read_entry(1, 3), 'red')
        self.game.put_chip(3, 'blue')
        self.assertEqual(self.game.read_entry(2, 3), 'blue')
        self.game.set_board_from_matrix(self.rows_on_corners_matrix)
        self.game.put_chip(5, 'red')
        self.assertEqual(self.game.read_entry(2, 5), 'red')
        with self.assertRaises(ColumnIsFull):
            self.game.put_chip(2, 'red')

    def test_read_entry(self):
        self.game.set_board_from_matrix(self.diagonals_on_corners_matrix)
        self.assertEqual(self.game.read_entry(1, 1), 'red')
        self.assertEqual(self.game.read_entry(2, 1), 'blue')
        self.assertEqual(self.game.read_entry(1, 2), 'blue')
        with self.assertRaises(OutOfIndex):
            self.game.read_entry(7, 1)
        with self.assertRaises(OutOfIndex):
            self.game.read_entry(1, 8)

    def test_set_board_from_matrix(self):
        self.assertTrue(self.game.set_board_from_matrix(self.diagonals_on_corners_matrix))
        self.assertFalse(self.game.set_board_from_matrix(self.invalid_matrix))

    def test_winner_exists_from_rows(self):
        self.game.set_board_from_matrix(self.rows_on_corners_matrix)
        self.assertEqual(self.game.winner_exists(), False)
        self.game.put_chip(7, 'red')
        self.assertEqual(self.game.winner_exists(), True)
        self.setUp()
        self.game.set_board_from_matrix(self.rows_on_corners_matrix)
        self.assertEqual(self.game.winner_exists(), False)
        self.game.put_chip(1, 'red')
        self.assertEqual(self.game.winner_exists(), True)

    def test_winner_exists_from_columns(self):
        self.game.set_board_from_matrix(self.columns_on_corners_matrix)
        self.assertEqual(self.game.winner_exists(), False)
        self.game.put_chip(7, 'blue')
        self.assertEqual(self.game.winner_exists(), True)
        self.setUp()
        self.game.set_board_from_matrix(self.columns_on_corners_matrix)
        self.assertEqual(self.game.winner_exists(), False)
        self.game.put_chip(1, 'blue')
        self.assertEqual(self.game.winner_exists(), True)

    def test_winner_exists_from_diagonals(self):
        self.game.set_board_from_matrix(self.diagonals_on_corners_matrix)
        self.assertEqual(self.game.winner_exists(), False)
        self.game.put_chip(7, 'red')
        self.assertEqual(self.game.winner_exists(), True)
        self.setUp()
        self.game.set_board_from_matrix(self.diagonals_on_corners_matrix)
        self.assertEqual(self.game.winner_exists(), False)
        self.game.put_chip(1, 'red')
        self.assertEqual(self.game.winner_exists(), True)


class TestMatch(unittest.TestCase):
    def setUp(self):
        self.match = Match()

    def test_automatic_playing(self):
        self.assertTrue(self.match.automatic_playing())


if __name__ == '__main__':
    unittest.main()
