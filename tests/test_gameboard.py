#!/usr/bin/env python
import unittest
from board_builder import BoardBuilder
from game.gameboard import GameBoard
from game.gameboard import ColumnIsFull
from game.gameboard import OutOfIndex

class TestGameBoard(unittest.TestCase):

    def setUp(self):
        self.builder = BoardBuilder('blue', 'red')
        self.empty_board = GameBoard()
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

        self.full_board = GameBoard.from_matrix([
                    ['blue',  'red', 'blue', 'blue', 'blue',  'red', 'blue'],
                    ['red',   'red', 'blue',  'red', 'blue',  'red', 'blue'],
                    ['blue', 'blue',  'red', 'blue',  'red', 'blue',  'red'],
                    ['red',  'blue',  'red',  'red',  'red', 'blue', 'blue'],
                    ['blue',  'red', 'blue', 'blue', 'blue',  'red',  'red'],
                    ['red',  'blue', 'blue',  'red', 'blue',  'red', 'blue']])

    def test_put_chip_on_empty_board(self):
        self.empty_board.put_chip(3, 'red')
        self.assertEqual(self.empty_board.read_entry(1, 3), 'red')
        self.empty_board.put_chip(3, 'blue')
        self.assertEqual(self.empty_board.read_entry(2, 3), 'blue')

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
        board = self.builder.build_from_moves(
            [1,1,2,2,1,1,2,2,1,1,2,2,4,3,4,4,3,3,4,4,3,
             3,4,3,5,5,5,5,5,6,6,6,6,6,6,7,7,7,7,7,7])
        """
        R R R B . R R
        B B R R B B B
        R R B B R R R
        B B R R B B B
        R R B B R R R
        B B R B B B B
        """
        board.put_chip(5, 'red')
        self.assertTrue(board.board_is_full())

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

    def test_validate_matrix_with_valid_matrix(self):
        self.assertTrue(self.empty_board.set_board_from_matrix([
            ['blue', 'blue', 'blue',  'red',   None,   None, None],
            ['red',   'red',  'red', 'blue', 'blue',   None, None],
            ['blue',  'red', 'blue',  'red', 'blue',   None, None],
            ['blue',  'red', 'blue',  'red',  'red',  'red', None],
            ['blue', 'blue',  'red', 'blue',  'red', 'blue', None],
            ['red',   'red',  'red', 'blue',  'red', 'blue', None]]))

    def test_validate_matrix_with_invalid_matrix_wrong_color(self):
        self.assertFalse(self.empty_board.set_board_from_matrix([
            ['blue', 'blue', 'blue',  'red',   None,     None, None],
            ['red',   'red',  'red', 'blue', 'blue',     None, None],
            ['blue',  'red', 'blue',  'red', 'blue', 'yellow', None],
            ['blue',  'red', 'blue',  'red',  'red',    'red', None],
            ['blue', 'blue',  'red', 'blue',  'red',   'blue', None],
            ['red',   'red',  'red', 'blue',  'red',   'blue', None]]))

    def test_validate_matrix_with_invalid_matrix_wrong_structure(self):
        self.assertFalse(self.empty_board.set_board_from_matrix([
            ['blue', 'blue', 'blue',  'red',   None,     None,  None],
            ['red',   'red',  'red', 'blue', 'blue',     None, 'blue'],
            ['blue',  'red', 'blue',  'red', 'blue',     None,  None],
            ['blue',  'red', 'blue',  'red',  'red',    'red',  None],
            ['blue', 'blue',  'red', 'blue',  'red',   'blue',  None],
            ['red',   'red',  'red', 'blue',  'red',   'blue',  None]]))

    def test_count_same_color_on_top_of_emtpy_column(self):
        board = GameBoard() # emtpy board
        self.assertEqual(0, board.count_same_color_on_top(1, 'blue'))

    def test_count_same_color_on_single_element_column(self):
        board = GameBoard.from_matrix([
                    [None,   None, None, None, None, None, None],
                    [None,   None, None, None, None, None, None],
                    [None,   None, None, None, None, None, None],
                    [None,   None, None, None, None, None, None],
                    [None,   None, None, None, None, None, None],
                    ['blue', None, None, None, None, None, None]])
        self.assertEqual(1, board.count_same_color_on_top(1, 'blue'))

    def test_count_same_color_on_column_with_multiple_chips(self):
        board = GameBoard.from_matrix([
                    [None,   None, None, None, None, None, None],
                    [None,   None, None, None, None, None, None],
                    ['blue', None, None, None, None, None, None],
                    ['blue', None, None, None, None, None, None],
                    ['blue', None, None, None, None, None, None],
                    ['blue', None, None, None, None, None, None]])
        self.assertEqual(4, board.count_same_color_on_top(1, 'blue'))

    def test_count_same_color_on_on_column_with_no_elements_of_desired_color(self):
        board = GameBoard.from_matrix([
                    [None,  None, None, None, None, None, None],
                    [None,  None, None, None, None, None, None],
                    [None,  None, None, None, None, None, None],
                    [None,  None, None, None, None, None, None],
                    ['red', None, None, None, None, None, None],
                    ['red', None, None, None, None, None, None]])
        self.assertEqual(0, board.count_same_color_on_top(1, 'blue'))

    def test_count_same_color_on_column_with_mixed_colors(self):
        board = GameBoard.from_matrix([
                    [None,   None, None, None, None, None, None],
                    ['blue', None, None, None, None, None, None],
                    ['blue', None, None, None, None, None, None],
                    ['blue', None, None, None, None, None, None],
                    ['red',  None, None, None, None, None, None],
                    ['red',  None, None, None, None, None, None]])
        self.assertEqual(3, board.count_same_color_on_top(1, 'blue'))

    def test_count_free_entries_on_empty_column(self):
        board = GameBoard() # empty board
        self.assertEqual(6, board.count_free_entries_on_column(2))

    def test_count_free_entries_on_full_column(self):
        board = GameBoard.from_matrix([
                    ['red',  None, None, None, None, None, None],
                    ['blue', None, None, None, None, None, None],
                    ['blue', None, None, None, None, None, None],
                    ['blue', None, None, None, None, None, None],
                    ['red',  None, None, None, None, None, None],
                    ['red',  None, None, None, None, None, None]])
        self.assertEqual(0, board.count_free_entries_on_column(1))

    def test_count_free_entries_on_almost_free_column(self):
        board = GameBoard.from_matrix([
                    [None,  None, None, None, None, None, None],
                    [None,  None, None, None, None, None, None],
                    [None,  None, None, None, None, None, None],
                    [None,  None, None, None, None, None, None],
                    [None,  None, None, None, None, None, None],
                    ['red', None, None, None, None, None, None]])
        self.assertEqual(5, board.count_free_entries_on_column(1))

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

    def test_get_rows(self):
        """Sets a gameboard matrix from a reference test_matrix, and then compares
           the value returned by the rows_iterator against each of its rows
        """
        test_matrix = [['blue', 'blue', 'blue',  'red',   None,   None,  None],
                       ['red',   'red',  'red', 'blue', 'blue',   None,  None],
                       ['blue',  'red', 'blue',  'red', 'blue',   None,  None],
                       ['blue',  'red', 'blue',  'red',  'red',  'red',  None],
                       ['blue', 'blue',  'red', 'blue',  'red', 'blue',  None],
                       ['red',   'red',  'red', 'blue',  'red', 'blue', 'blue']]
        board = GameBoard.from_matrix(test_matrix)
        for index, row in enumerate(board.get_rows()):
            self.assertEqual(row, test_matrix[index])

    def test_is_column_full(self):
        self.assertFalse(self.empty_board.is_column_full(1))
        self.assertFalse(self.empty_board.is_column_full(4))
        self.assertFalse(self.empty_board.is_column_full(7))

        board = GameBoard.from_matrix([
                    ['blue', None,   None,   'red',   None,    None,   'red'],
                    ['red',  'red',  None,   'blue', 'blue',   None,  'blue'],
                    ['blue', 'blue', 'red',  'red',   'red',  'blue',  'red'],
                    ['red',  'red',  'blue', 'blue', 'blue',   'red', 'blue'],
                    ['blue', 'blue',  'red', 'red',   'red',  'blue',  'red'],
                    ['red',  'red',  'blue', 'blue',  'blue',  'red', 'blue']])
        self.assertTrue(board.is_column_full(1))
        self.assertFalse(board.is_column_full(2))
        self.assertFalse(board.is_column_full(3))
        self.assertTrue(board.is_column_full(4))
        self.assertFalse(board.is_column_full(5))
        self.assertFalse(board.is_column_full(6))
        self.assertTrue(board.is_column_full(7))

    def test_playable_positions(self):
        self.assertEqual(self.empty_board.playable_positions(), [1,2,3,4,5,6,7])
        self.assertEqual(self.full_board.playable_positions(), [])
        board = GameBoard.from_matrix([
                    [None , 'blue',  None,   'red',   None,    'red',  None ],
                    ['red',  'red',  None,   'blue', 'blue',  'blue', 'blue'],
                    ['blue', 'blue', 'red',  'red',   'red',  'blue',  'red'],
                    ['red',  'red',  'blue', 'blue', 'blue',   'red', 'blue'],
                    ['blue', 'blue',  'red', 'red',   'red',  'blue',  'red'],
                    ['red',  'red',  'blue', 'blue',  'blue',  'red', 'blue']])
        self.assertEqual(board.playable_positions(), [1,3,5,7])

    def test_copy(self):
        empty_copy = self.empty_board.copy()
        self.assertFalse(self.empty_board is empty_copy)
        self.assertEqual(self.empty_board, empty_copy)

        self.empty_board.put_chip(1, 'red')
        self.assertNotEqual(self.empty_board, empty_copy)
        empty_copy.put_chip(1, 'red')
        self.assertEqual(self.empty_board, empty_copy)

    def test_undo_move(self):
        board = self.builder.build_from_moves([1])
        board.undo_move()
        self.assertEqual(self.empty_board, board)

        test_board = self.builder.build_from_moves([1,2,3,4,5,6,7,1])
        expected_board = self.builder.build_from_moves([1,2,3,4,5,6,7])
        test_board.undo_move()
        self.assertEqual(expected_board, test_board)

        test_board = self.builder.build_from_moves([1,1,1,1,1,1])
        expected_board = self.builder.build_from_moves([1,1,1,1,1])
        test_board.undo_move()
        self.assertEqual(expected_board, test_board)

        test_board = self.builder.build_from_moves([1,2,3])
        expected_board_1 = self.builder.build_from_moves([1,2])
        test_board.undo_move()
        self.assertEqual(expected_board_1, test_board)

        test_board.put_chip(4, 'blue')
        expected_board_2 = self.builder.build_from_moves([1,2,4])
        self.assertEqual(expected_board_2, test_board)

        test_board.undo_move()
        self.assertEqual(expected_board_1, test_board)

        test_board = self.builder.build_from_moves([1,2,3,4,5,6,7])
        for i in range(7):
            test_board.undo_move()
        self.assertEqual(self.empty_board, test_board)

    def test_winner_color_in_columns(self):
        self._test_winner_in_columns('winner_color')

    def test_winner_color_in_rows(self):
        self._test_winner_in_rows('winner_color')

    def test_winner_color_in_diagonals(self):
        self._test_winner_in_diagonals('winner_color')

    def test_winner_color_in_last_move_in_columns(self):
        self._test_winner_in_columns('winner_color_in_last_move')

    def test_winner_color_in_last_move_in_rows(self):
        self._test_winner_in_rows('winner_color_in_last_move')

    def test_winner_color_in_last_move_in_diagonals(self):
        self._test_winner_in_diagonals('winner_color_in_last_move')

    def _test_winner_in_columns(self, winner_method):
        board = self.builder.build_from_moves([1,2,1,3,1,4,1])
        """
        . . . . . . .
        . . . . . . .
        B . . . . . .
        B . . . . . .
        B . . . . . .
        B R R R . . .
        """
        self.assertEquals(getattr(board, winner_method)(), 'blue')

        board = self.builder.build_from_moves([7,1,7,7,1,7,2,7,3,7])
        """
        . . . . . . R
        . . . . . . R
        . . . . . . R
        . . . . . . R
        B . . . . . B
        R B B . . . B
        """
        self.assertEquals(getattr(board, winner_method)(), 'red')

    def _test_winner_in_rows(self, winner_method):
        board = self.builder.build_from_moves([1,6,2,6,3,7,4])
        """
        . . . . . . .
        . . . . . . .
        . . . . . . .
        . . . . . . .
        . . . . . R .
        B B B B . R R
        """
        self.assertEquals(getattr(board, winner_method)(), 'blue')

        board = self.builder.build_from_moves([7,6,5,4,6,5,4,7,5,4,7,6,5,4,7,6,6,5,4,7,1,7,2,6,1,5,2,4])
        """
        . . . R R R R
        . . . B R B R
        . . . R B R B
        . . . R B R B
        B B . B R B R
        B B . R B R B
        """
        self.assertEquals(getattr(board, winner_method)(), 'red')

    def _test_winner_in_diagonals(self, winner_method):
        board = self.builder.build_from_moves([1,1,1,2,1,2,2,3,3,7,4])
        """
        . . . . . . .
        . . . . . . .
        B . . . . . .
        B B . . . . .
        R R B . . . .
        B R R B . . R
        """
        self.assertEquals(getattr(board, winner_method)(), 'blue')

        board = self.builder.build_from_moves([1,1,1,1,1,1,2,3,2,2,2,2,3,3,4,3,4,4])
        """
        R . . . . . .
        B R . . . . .
        R B R . . . .
        B R R R . . .
        R B B B . . .
        B B R B . . .
        """
        self.assertEquals(getattr(board, winner_method)(), 'red')

        board = self.builder.build_from_moves([1,7,6,6,5,4,5,5,4,4,1,4])
        """
        . . . . . . .
        . . . . . . .
        . . . R . . .
        . . . R R . .
        B . . B B R .
        B . . R B B R
        """
        self.assertEquals(getattr(board, winner_method)(), 'red')

        board = self.builder.build_from_moves([7,7,7,6,6,6,6,5,5,5,1,5,5,4,4,4,4,2,4,2,4])
        """
        . . . B . . .
        . . . B B . .
        . . . B R B .
        . . . R R R B
        . R . B B B R
        B R . R R R B
        """
        self.assertEquals(getattr(board, winner_method)(), 'blue')

        board = self.builder.build_from_moves([7,7,7,6,7,6,6,5,5,1,4])
        """
        . . . . . . .
        . . . . . . .
        . . . . . . B
        . . . . . B B
        . . . . B R R
        R . . B R R B
        """
        self.assertEquals(getattr(board, winner_method)(), 'blue')


        board = self.builder.build_from_moves([7,7,7,7,7,7,6,5,6,6,6,6,5,5,4,5,4,4])
        """
        . . . . . . R
        . . . . . R B
        . . . . R B R
        . . . R R R B
        . . . B B B R
        . . . B R B B
        """
        self.assertEquals(getattr(board, winner_method)(), 'red')

        board = self.builder.build_from_moves([1,1,1,2,2,2,2,3,3,3,7,3,3,4,4,4,4,6,4,6,4])
        """
        . . . B . . .
        . . B B . . .
        . B R B . . .
        B R R R . . .
        R B B B . R .
        B R R R . R B
        """
        self.assertEquals(getattr(board, winner_method)(), 'blue')

        board = self.builder.build_from_moves([1,1,1,2,2,2,2,4,4,4,7,4,4,3,3,3,3,6,3,6,4])
        """
        . . . B . . .
        . . B B . . .
        . B B R . . .
        B R R R . . .
        R B B B . R .
        B R R R . R B
        """
        self.assertEquals(getattr(board, winner_method)(), 'blue')

    def test_is_valid_move_on_valid_column(self):
        test_board = self.builder.build_from_moves([1,1,1,1,1])
        self.assertTrue(test_board.is_valid_move(1))

    def test_is_valid_move_on_invalid_column(self):
        test_board = self.builder.build_from_moves([2,2,2,2,2,2])
        self.assertFalse(test_board.is_valid_move(2))
