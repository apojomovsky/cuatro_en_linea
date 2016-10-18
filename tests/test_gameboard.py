#!/usr/bin/env python

import unittest
from game.gameboard import GameBoard
from game.gameboard import ColumnIsFull
from game.gameboard import OutOfIndex

class TestGameBoard(unittest.TestCase):

    def setUp(self):
        self.board = GameBoard()
        self.board_test_rows = GameBoard.from_matrix([
                    [None,   'red',  'red',  'red',   None,   None, None],
                    ['red', 'blue',  'red', 'blue',   None,   None, None],
                    ['blue', 'red', 'blue',  'red',   None,   None, None],
                    ['blue', 'red',  'red', 'blue',   None,   None, None],
                    ['red', 'blue',  'red', 'blue',   None,   None, None],
                    ['blue', 'red', 'blue',  'red',  'red',  'red', None]])
        self.board_test_columns = GameBoard.from_matrix([
                    [None,   None, None, None, None, None,   None],
                    ['blue', None, None, None, None, None, 'blue'],
                    ['blue', None, None, None, None, None, 'blue'],
                    ['blue', None, None, None, None, None, 'blue'],
                    ['red',  None, None, None, None, None,  'red'],
                    ['red',  None, None, None, None, None,  'red']])
        self.board_test_diagonals = GameBoard.from_matrix([
                    [None,     None,   None,   None,   None,   None,   None],
                    ['red',   'red',   None,   None,   None,  'red', 'blue'],
                    ['blue', 'blue',  'red',   None,  'red', 'blue',  'red'],
                    ['red',  'blue',  'red',  'red',  'red', 'blue', 'blue'],
                    ['blue',  'red', 'blue', 'blue', 'blue',  'red',  'red'],
                    ['red',  'blue', 'blue',  'red', 'blue',  'red', 'blue']])

        self.board_almost_full = GameBoard.from_matrix([
                    ['blue',  'red', 'blue',   None, 'blue',  'red', 'blue'],
                    ['red',   'red', 'blue',  'red', 'blue',  'red', 'blue'],
                    ['blue', 'blue',  'red', 'blue',  'red', 'blue',  'red'],
                    ['red',  'blue',  'red',  'red',  'red', 'blue', 'blue'],
                    ['blue',  'red', 'blue', 'blue', 'blue',  'red',  'red'],
                    ['red',  'blue', 'blue',  'red', 'blue',  'red', 'blue']])

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

    def test_put_chip_on_first_non_full_column_from_left_to_right(self):
        self.board_test_rows.put_chip_on_first_non_full_column('red')
        self.assertEqual(self.board_test_rows.read_entry(6, 1), 'red')
        self.board_test_rows.put_chip_on_first_non_full_column('red')
        self.assertEqual(self.board_test_rows.read_entry(2, 5), 'red')

    def test_put_chip_on_first_non_full_column_from_right_to_left(self):
        self.board_test_columns.put_chip_on_first_non_full_column('red', True)
        self.assertEqual(self.board_test_columns.read_entry(6, 7), 'red')
        self.board_test_columns.put_chip_on_first_non_full_column('red', True)
        self.assertEqual(self.board_test_columns.read_entry(1, 6), 'red')

    def test_put_chip_on_first_non_full_row_from_left_to_right(self):
        self.board_test_rows.put_chip_on_first_non_full_row('red')
        self.assertEqual(self.board_test_rows.read_entry(1, 7), 'red')
        self.board_test_rows.put_chip_on_first_non_full_row('red')
        self.assertEqual(self.board_test_rows.read_entry(2, 5), 'red')

    def test_put_chip_on_first_non_full_row_from_right_to_left(self):
        self.board_test_columns.put_chip_on_first_non_full_row('red', True)
        self.assertEqual(self.board_test_columns.read_entry(1, 7), 'red')
        self.board_test_columns.put_chip_on_first_non_full_row('red', True)
        self.assertEqual(self.board_test_columns.read_entry(2, 7), 'red')
        self.board_test_columns.put_chip_on_first_non_full_row('red', True)
        self.assertEqual(self.board_test_columns.read_entry(2, 7), 'red')

    def test_read_entry_from_valid_position(self):
        self.assertEqual(self.board_test_diagonals.read_entry(1, 1), 'red')
        self.assertEqual(self.board_test_diagonals.read_entry(2, 1), 'blue')
        self.assertEqual(self.board_test_diagonals.read_entry(1, 2), 'blue')

    def test_read_entry_from_invalid_position(self):
        with self.assertRaises(OutOfIndex):
            self.board_test_diagonals.read_entry(7, 1)
        with self.assertRaises(OutOfIndex):
            self.board_test_diagonals.read_entry(1, 8)

    def test_column_is_full(self):
        self.assertFalse(self.board_test_diagonals.column_is_full(1))
        self.board_test_diagonals.put_chip(1, 'blue')
        self.assertTrue(self.board_test_diagonals.column_is_full(1))
        self.assertFalse(self.board_test_diagonals.column_is_full(7))
        self.board_test_diagonals.put_chip(7, 'blue')
        self.assertTrue(self.board_test_diagonals.column_is_full(7))

    def test_board_is_full(self):
        self.assertFalse(self.board_test_columns.board_is_full())
        self.board_almost_full.put_chip(4, 'blue')
        self.assertTrue(self.board_almost_full.board_is_full())

    def test_game_over_on_full_board(self):
        self.assertFalse(self.board_test_columns.game_over())
        self.board_almost_full.put_chip(4, 'blue')
        self.assertTrue(self.board_almost_full.game_over())

    def test_game_over_on_winner(self):
        self.assertEqual(self.board_test_rows.game_over(), False)
        self.board_test_rows.put_chip(1, 'red')
        self.assertEqual(self.board_test_rows.game_over(), True)

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
