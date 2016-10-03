#!/usr/bin/env python

import unittest
import numpy
from gameboard import GameBoard
from gameboard import ColumnIsFull
from gameboard import OutOfIndex
from match import Match


class TestGameBoard(unittest.TestCase):

    def setUp(self):
        self.board = GameBoard()

        self.board_test_rows = GameBoard.from_matrix(numpy.array([
                    ['-',    'red',  'red',  'red',   '-',   '-', '-'],
                    ['red', 'blue',  'red', 'blue',   '-',   '-', '-'],
                    ['blue', 'red', 'blue',  'red',   '-',   '-', '-'],
                    ['blue', 'red',  'red', 'blue',   '-',   '-', '-'],
                    ['red', 'blue',  'red', 'blue',   '-',   '-', '-'],
                    ['blue', 'red', 'blue',  'red', 'red', 'red', '-']], dtype='a5'))

        self.board_test_columns = GameBoard.from_matrix(numpy.array([
                    ['-',    '-', '-', '-', '-', '-',    '-'],
                    ['blue', '-', '-', '-', '-', '-', 'blue'],
                    ['blue', '-', '-', '-', '-', '-', 'blue'],
                    ['blue', '-', '-', '-', '-', '-', 'blue'],
                    ['red',  '-', '-', '-', '-', '-',  'red'],
                    ['red',  '-', '-', '-', '-', '-',  'red']], dtype='a5'))

        self.board_test_diagonals = GameBoard.from_matrix(numpy.array([
                    ['-',       '-',    '-',    '-',    '-',    '-',    '-'],
                    ['red',   'red',    '-',    '-',    '-',  'red', 'blue'],
                    ['blue', 'blue',  'red',    '-',  'red', 'blue',  'red'],
                    ['red',  'blue',  'red',  'red',  'red', 'blue', 'blue'],
                    ['blue',  'red', 'blue', 'blue', 'blue',  'red',  'red'],
                    ['red',  'blue', 'blue',  'red', 'blue',  'red', 'blue']], dtype='a5'))

    def test_put_chip_on_empty_board(self):
        self.board.put_chip(3, 'red')
        self.assertEqual(self.board.read_entry(1, 3), 'red')
        self.board.put_chip(3, 'blue')
        self.assertEqual(self.board.read_entry(2, 3), 'blue')

    def test_put_chip_on_column_with_one_element(self):
        self.board_test_rows.put_chip(5, 'red')
        self.assertEqual(self.board_test_rows.read_entry(2, 5), 'red')

    def test_put_chip_on_column_almost_full(self):
        self.board_test_columns.put_chip(1, 'red')
        self.assertEqual(self.board_test_columns.read_entry(6, 1), 'red')

    def test_put_chip_on_full_column(self):
        with self.assertRaises(ColumnIsFull):
            self.board_test_rows.put_chip(2, 'red')

    def test_read_entry_from_valid_position(self):
        self.assertEqual(self.board_test_diagonals.read_entry(1, 1), 'red')
        self.assertEqual(self.board_test_diagonals.read_entry(2, 1), 'blue')
        self.assertEqual(self.board_test_diagonals.read_entry(1, 2), 'blue')

    def test_read_entry_from_invalid_position(self):
        with self.assertRaises(OutOfIndex):
            self.board_test_diagonals.read_entry(7, 1)
        with self.assertRaises(OutOfIndex):
            self.board_test_diagonals.read_entry(1, 8)

    def test_winner_exists_from_rows_on_left_corner(self):
        self.assertEqual(self.board_test_rows.winner_exists(), False)
        self.board_test_rows.put_chip(1, 'red')
        self.assertEqual(self.board_test_rows.winner_exists(), True)

    def test_winner_exists_from_rows_on_right_corner(self):
        self.assertEqual(self.board_test_rows.winner_exists(), False)
        self.board_test_rows.put_chip(7, 'red')
        self.assertEqual(self.board_test_rows.winner_exists(), True)

    def test_winner_exists_from_columns_on_left_corner(self):
        self.assertEqual(self.board_test_columns.winner_exists(), False)
        self.board_test_columns.put_chip(1, 'blue')
        self.assertEqual(self.board_test_columns.winner_exists(), True)

    def test_winner_exists_from_columns_on_right_corner(self):
        self.assertEqual(self.board_test_columns.winner_exists(), False)
        self.board_test_columns.put_chip(7, 'blue')
        self.assertEqual(self.board_test_columns.winner_exists(), True)

    def test_winner_exists_from_diagonals_on_left_corner(self):
        self.assertEqual(self.board_test_diagonals.winner_exists(), False)
        self.board_test_diagonals.put_chip(1, 'red')
        self.assertEqual(self.board_test_diagonals.winner_exists(), True)

    def test_winner_exists_from_diagonals_on_right_corner(self):
        self.assertEqual(self.board_test_diagonals.winner_exists(), False)
        self.board_test_diagonals.put_chip(7, 'red')
        self.assertEqual(self.board_test_diagonals.winner_exists(), True)


class TestMatch(unittest.TestCase):
    def setUp(self):
        self.match = Match()

    def test_automatic_playing(self):
        self.assertTrue(self.match.automatic_playing())


if __name__ == '__main__':
    unittest.main()
