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
        self.assertFalse(self.board_test_columns.is_game_over())
        self.board_almost_full.put_chip(4, 'blue')
        self.assertTrue(self.board_almost_full.is_game_over())

    def test_game_over_on_winner(self):
        self.assertEqual(self.board_test_rows.is_game_over(), False)
        self.board_test_rows.put_chip(1, 'red')
        self.assertEqual(self.board_test_rows.is_game_over(), True)

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

    def test_equality_of_empty_boards(self):
        board_1 = GameBoard()
        board_2 = GameBoard()
        self.assertTrue(board_1 == board_2)

    def test_equality_of_two_loaded_boards(self):
        board_1 = GameBoard.from_matrix([
                    ['blue', 'blue', 'blue',  'red',   None,   None, None],
                    ['red',   'red',  'red', 'blue', 'blue',   None, None],
                    ['blue',  'red', 'blue',  'red', 'blue',   None, None],
                    ['blue',  'red', 'blue',  'red',  'red',  'red', None],
                    ['blue', 'blue',  'red', 'blue',  'red', 'blue', None],
                    ['red',   'red',  'red', 'blue',  'red', 'blue', None]])
        board_2 = GameBoard.from_matrix([
                    ['blue', 'blue', 'blue',  'red',   None,   None, None],
                    ['red',   'red',  'red', 'blue', 'blue',   None, None],
                    ['blue',  'red', 'blue',  'red', 'blue',   None, None],
                    ['blue',  'red', 'blue',  'red',  'red',  'red', None],
                    ['blue', 'blue',  'red', 'blue',  'red', 'blue', None],
                    ['red',   'red',  'red', 'blue',  'red', 'blue', None]])
        self.assertTrue(board_1 == board_2)

    def test_equality_of_boards_loaded_with_a_same_given_matrix(self):
        matrix = [['blue', 'blue', 'blue',  'red',   None,   None, None],
                  ['red',   'red',  'red', 'blue', 'blue',   None, None],
                  ['blue',  'red', 'blue',  'red', 'blue',   None, None],
                  ['blue',  'red', 'blue',  'red',  'red',  'red', None],
                  ['blue', 'blue',  'red', 'blue',  'red', 'blue', None],
                  ['red',   'red',  'red', 'blue',  'red', 'blue', None]]
        board_1 = GameBoard.from_matrix(matrix)
        board_2 = GameBoard.from_matrix(matrix)
        self.assertTrue(board_1 == board_2)

    def test_unequality_of_very_similar_boards(self):
        board_1 = GameBoard.from_matrix([
                    ['blue', 'blue', 'blue',  'red',   None,   None, None],
                    ['red',   'red',  'red', 'blue', 'blue',   None, None],
                    ['blue',  'red', 'blue',  'red', 'blue',   None, None],
                    ['blue',  'red', 'blue',  'red',  'red',  'red', None],
                    ['blue', 'blue',  'red', 'blue',  'red', 'blue', None],
                    ['red',   'red',  'red', 'blue',  'red', 'blue', 'red']])
        board_2 = GameBoard.from_matrix([
                    ['blue', 'blue', 'blue',  'red',   None,   None,  None],
                    ['red',   'red',  'red', 'blue', 'blue',   None,  None],
                    ['blue',  'red', 'blue',  'red', 'blue',   None,  None],
                    ['blue',  'red', 'blue',  'red',  'red',  'red',  None],
                    ['blue', 'blue',  'red', 'blue',  'red', 'blue',  None],
                    ['red',   'red',  'red', 'blue',  'red', 'blue', 'blue']])
        self.assertTrue(board_1 != board_2)
