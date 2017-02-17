#!/usr/bin/env python
import unittest
from board_builder import BoardBuilder
from game.gameboard import GameBoard
from game.gameboard import ColumnIsFull
from game.gameboard import OutOfIndex

class TestGameBoard(unittest.TestCase):
    def setUp(self):
        self.builder = BoardBuilder('W', 'B')
        self.board_empty = GameBoard()

    def get_almost_full_board(self):
        """
        W W W B . B B
        B B W W B W W
        W W B B W B B
        B B W W B W W
        W W B B W B B
        B B W B B W W
        """
        return self.builder.build_from_moves(
            [1,1,2,2,1,1,2,2,1,1,2,2,4,3,4,4,3,3,4,4,3,
             3,4,3,5,5,5,5,5,6,6,6,6,6,6,7,7,7,7,7,7])

    def get_full_board(self):
        """
        W W W B W B B
        B B W W B W W
        W W B B W B B
        B B W W B W W
        W W B B W B B
        B B W B B W W
        """
        return self.builder.build_from_moves(
            [1,1,2,2,1,1,2,2,1,1,2,2,4,3,4,4,3,3,4,4,3,
             3,4,3,5,5,5,5,5,6,6,6,6,6,6,7,7,7,7,7,7,5])

    def get_board_with_white_about_to_win(self):
        """
        . . . . . . .
        . . . . . . .
        . . . . . . .
        W B . . . . .
        W B . . . . .
        W B . . . . .
        """
        return self.builder.build_from_moves([1,2,1,2,1,2])

    def test_put_chip_on_empty_board(self):
        self.board_empty.put_chip(3, 'B')
        self.assertEqual(self.board_empty.read_entry(1, 3), 'B')

    def test_put_chip_on_column_with_one_element(self):
        board_with_one_element = self.builder.build_from_moves([1])
        """
        . . . . . . .
        . . . . . . .
        . . . . . . .
        . . . . . . .
        . . . . . . .
        B . . . . . .
        """
        board_with_one_element.put_chip(1, 'B')
        self.assertEqual(board_with_one_element.read_entry(2, 1), 'B')

    def test_put_chip_on_column_almost_full(self):
        almost_full_board = self.get_almost_full_board()
        almost_full_board.put_chip(5, 'B')
        self.assertEqual(almost_full_board.read_entry(6, 5), 'B')

    def test_put_chip_on_full_column(self):
        almost_full_board = self.get_almost_full_board()
        with self.assertRaises(ColumnIsFull):
            almost_full_board.put_chip(2, 'B')

    def test_read_entry_on_lowest_right_corner(self):
        almost_full_board = self.get_almost_full_board()
        self.assertEqual(almost_full_board.read_entry(6, 7), 'W')

    def test_read_entry_on_upper_right_corner(self):
        full_board = self.get_full_board()
        self.assertEqual(full_board.read_entry(1, 7), 'B')

    def test_read_entry_on_upper_left_corner(self):
        full_board = self.get_full_board()
        self.assertEqual(full_board.read_entry(1, 1), 'W')

    def test_read_entry_from_inexistent_row(self):
        with self.assertRaises(OutOfIndex):
            self.board_empty.read_entry(7, 1)

    def test_read_entry_from_inexistent_column(self):
        with self.assertRaises(OutOfIndex):
            self.board_empty.read_entry(3, 8)

    def test_column_is_full(self):
        almost_full_board = self.get_almost_full_board()
        self.assertTrue(almost_full_board.column_is_full(7))

    def test_board_is_full_on_empty_board(self):
        self.assertFalse(self.board_empty.board_is_full())

    def test_board_is_full(self):
        full_board = self.get_full_board()
        self.assertTrue(full_board.board_is_full())

    def test_game_over_on_full_board(self):
        full_board = self.get_full_board()
        self.assertTrue(full_board.is_game_over())

    def test_game_over_on_winner(self):
        """
        . . . . . . .
        . . . . . . .
        . . . . . . .
        W B . . . . .
        W B . . . . .
        W B . . . . .
        """
        about_to_win_board = self.get_board_with_white_about_to_win()
        about_to_win_board.put_chip(1, 'W')
        self.assertEqual(about_to_win_board.is_game_over(), True)

    def test_winner_exists_from_rows_on_left_corner(self):
        test_board = self.builder.build_from_moves([2,7,3,7,4,7])
        """
        . . . . . . .
        . . . . . . .
        . . . . . . B
        . . . . . . B
        . W W W . . B
        """
        test_board.put_chip(1, 'W')
        self.assertEqual(test_board.winner_exists(), True)

    def test_winner_exists_from_rows_on_right_corner(self):
        test_board = self.builder.build_from_moves([6,1,5,1,4,1])
        """
        . . . . . . .
        . . . . . . .
        B . . . . . .
        B . . . . . .
        B . . W W W .
        """
        test_board.put_chip(7, 'W')
        self.assertEqual(test_board.winner_exists(), True)

    def test_winner_exists_from_columns_on_left_corner(self):
        test_board = self.builder.build_from_moves([1,2,1,3,1,4])
        """
        . . . . . . .
        . . . . . . .
        W . . . . . .
        W . . . . . .
        W B B B . . .
        """
        test_board.put_chip(1, 'W')
        self.assertEqual(test_board.winner_exists(), True)

    def test_winner_exists_from_columns_on_right_corner(self):
        test_board = self.builder.build_from_moves([7,1,7,2,7,3])
        """
        . . . . . . .
        . . . . . . .
        . . . . . . W
        . . . . . . W
        B B B . . . W
        """
        test_board.put_chip(7, 'W')
        self.assertEqual(test_board.winner_exists(), True)

    def test_winner_exists_from_diagonals_on_left_corner(self):
        test_board = self.builder.build_from_moves([1,2,1,2,1,2,2,1,6,3,3,6,3,3,7,4,4,5])
        test_board.put_chip(1, 'W')
        self.assertEqual(test_board.winner_exists(), True)

    def test_winner_exists_from_diagonals_on_right_corner(self):
        test_board = self.builder.build_from_moves([7,6,7,6,7,6,6,7,2,5,5,2,5,5,1,4,4,3])
        """
        . . . . . . .
        . . . . B W B
        . . . . W B W
        . B . W W B W
        W W B B B B W
        """
        test_board.put_chip(7, 'W')
        self.assertEqual(test_board.winner_exists(), True)

    def test_validate_matrix_with_valid_matrix(self):
        self.assertTrue(self.board_empty.set_board_from_matrix([
            ['W', 'W', 'W', 'B',  None, None, None],
            ['B', 'B', 'B', 'W',   'W', None, None],
            ['W', 'B', 'W', 'B',   'W', None, None],
            ['W', 'B', 'W', 'B',   'B',  'B', None],
            ['W', 'W', 'B', 'W',   'B',  'W', None],
            ['B', 'B', 'B', 'W',   'B',  'W', None]]))

    def test_validate_matrix_with_invalid_matrix_wrong_color(self):
        self.assertFalse(self.board_empty.set_board_from_matrix([
            ['W', 'W', 'W', 'B', None,     None, None],
            ['B', 'B', 'B', 'W',  'W',     None, None],
            ['W', 'B', 'W', 'B',  'W', 'yellow', None],
            ['W', 'B', 'W', 'B',  'B',      'B', None],
            ['W', 'W', 'B', 'W',  'B',      'W', None],
            ['B', 'B', 'B', 'W',  'B',      'W', None]]))

    def test_validate_matrix_with_invalid_matrix_wrong_structure(self):
        self.assertFalse(self.board_empty.set_board_from_matrix([
            ['W', 'W', 'W', 'B', None, None, None],
            ['B', 'B', 'B', 'W',  'W', None,  'W'],
            ['W', 'B', 'W', 'B',  'W', None, None],
            ['W', 'B', 'W', 'B',  'B',  'B', None],
            ['W', 'W', 'B', 'W',  'B',  'W', None],
            ['B', 'B', 'B', 'W',  'B',  'W', None]]))

    def test_count_same_color_on_top_of_empty_column(self):
        board = GameBoard() # empty board
        self.assertEqual(0, board.count_same_color_on_top(1, 'W'))

    def test_count_same_color_on_single_element_column(self):
        test_board = self.builder.build_from_moves([1])
        """
        . . . . . . .
        . . . . . . .
        . . . . . . .
        . . . . . . .
        W . . . . . .
        """
        self.assertEqual(1, test_board.count_same_color_on_top(1, 'W'))

    def test_count_same_color_on_column_with_multiple_chips(self):
        test_board = self.get_board_with_white_about_to_win()
        """
        . . . . . . .
        . . . . . . .
        W B . . . . .
        W B . . . . .
        W B . . . . .
        """
        self.assertEqual(3, test_board.count_same_color_on_top(1, 'W'))

    def test_count_same_color_on_top_on_column_with_no_elements_of_desired_color(self):
        test_board = self.get_board_with_white_about_to_win()
        """
        . . . . . . .
        . . . . . . .
        W B . . . . .
        W B . . . . .
        W B . . . . .
        """
        self.assertEqual(0, test_board.count_same_color_on_top(1, 'R'))

    def test_count_same_color_on_column_with_mixed_colors(self):
        test_board = self.builder.build_from_moves([1,1,1,2,2,1,2])
        """
        . . . . . . .
        B . . . . . .
        W W . . . . .
        B W . . . . .
        W B . . . . .
        """
        self.assertEqual(2, test_board.count_same_color_on_top(2, 'W'))

    def test_count_free_entries_on_empty_column(self):
        board = GameBoard()
        self.assertEqual(6, board.count_free_entries_on_column(2))

    def test_count_free_entries_on_full_column(self):
        test_board = self.builder.build_from_moves([1,1,1,1,1,1])
        """
        W . . . . . .
        B . . . . . .
        W . . . . . .
        B . . . . . .
        W . . . . . .
        """
        self.assertEqual(0, test_board.count_free_entries_on_column(1))

    def test_count_free_entries_on_almost_free_column(self):
        board_with_one_element = self.builder.build_from_moves([1])
        """
        . . . . . . .
        . . . . . . .
        . . . . . . .
        . . . . . . .
        . . . . . . .
        B . . . . . .
        """
        self.assertEqual(5, board_with_one_element.count_free_entries_on_column(1))

    def test_equality_of_empty_boards(self):
        board_1 = GameBoard()
        board_2 = GameBoard()
        self.assertTrue(board_1 == board_2)

    def test_equality_of_two_loaded_boards(self):
        board_1 = self.get_full_board()
        board_2 = self.get_full_board()
        self.assertTrue(board_1 == board_2)

    def test_equality_of_boards_loaded_with_a_same_given_matrix(self):
        matrix = [['W', 'W', 'W', 'B', None, None, None],
                  ['B', 'B', 'B', 'W',  'W', None, None],
                  ['W', 'B', 'W', 'B',  'W', None, None],
                  ['W', 'B', 'W', 'B',  'B',  'B', None],
                  ['W', 'W', 'B', 'W',  'B',  'W', None],
                  ['B', 'B', 'B', 'W',  'B',  'W', None]]
        board_1 = GameBoard.from_matrix(matrix)
        board_2 = GameBoard.from_matrix(matrix)
        self.assertTrue(board_1 == board_2)

    def test_unequality_of_very_similar_boards(self):
        board_1 = self.get_full_board()
        """
        W W B B W B B
        B B W W B W W
        W W B B W B B
        B B W W B W W
        W W B W W B B
        """
        board_2 = self.get_almost_full_board()
        """
        B B B W . W W
        W W B B W B B
        B B W W B W W
        W W B B W B B
        B B W W B W W
        W W B W W B B
        """
        self.assertTrue(board_1 != board_2)

    def test_get_rows(self):
        """Sets a gameboard matrix from a reference test_matrix, and then compares
           the value returned by the rows_iterator against each of its rows
        """
        test_matrix = [['W', 'W', 'W', 'B', None, None, None],
                       ['B', 'B', 'B', 'W',  'W', None, None],
                       ['W', 'B', 'W', 'B',  'W', None, None],
                       ['W', 'B', 'W', 'B',  'B',  'B', None],
                       ['W', 'W', 'B', 'W',  'B',  'W', None],
                       ['B', 'B', 'B', 'W',  'B',  'W',  'W']]
        board = GameBoard.from_matrix(test_matrix)
        for index, row in enumerate(board.get_rows()):
            self.assertEqual(row, test_matrix[index])

    def test_is_column_full(self):
        self.assertFalse(self.board_empty.is_column_full(1))
        self.assertFalse(self.board_empty.is_column_full(4))
        self.assertFalse(self.board_empty.is_column_full(7))
        board = GameBoard.from_matrix([
                    ['W', None, None, 'B', None, None, 'B'],
                    ['B',  'B', None, 'W',  'W', None, 'W'],
                    ['W',  'W',  'B', 'B',  'B',  'W', 'B'],
                    ['B',  'B',  'W', 'W',  'W',  'B', 'W'],
                    ['W',  'W',  'B', 'B',  'B',  'W', 'B'],
                    ['B',  'B',  'W', 'W',  'W',  'B', 'W']])
        self.assertTrue(board.is_column_full(1))
        self.assertFalse(board.is_column_full(2))
        self.assertFalse(board.is_column_full(3))
        self.assertTrue(board.is_column_full(4))
        self.assertFalse(board.is_column_full(5))
        self.assertFalse(board.is_column_full(6))
        self.assertTrue(board.is_column_full(7))

    def test_playable_positions(self):
        self.assertEqual(self.board_empty.playable_positions(), [1,2,3,4,5,6,7])
        self.assertEqual(self.get_full_board().playable_positions(), [])
        board = GameBoard.from_matrix([
                    [None, 'W',  None, 'B', None, 'B', None ],
                    ['B' , 'B',  None, 'W',  'W', 'W',   'W'],
                    ['W' , 'W',   'B', 'B',  'B', 'W',   'B'],
                    ['B' , 'B',   'W', 'W',  'W', 'B',   'W'],
                    ['W' , 'W',   'B', 'B',  'B', 'W',   'B'],
                    ['B' , 'B',   'W', 'W',  'W', 'B',   'W']])
        self.assertEqual(board.playable_positions(), [1,3,5,7])

    def test_copy(self):
        empty_copy = self.board_empty.copy()
        self.assertFalse(self.board_empty is empty_copy)
        self.assertEqual(self.board_empty, empty_copy)

        self.board_empty.put_chip(1, 'B')
        self.assertNotEqual(self.board_empty, empty_copy)
        empty_copy.put_chip(1, 'B')
        self.assertEqual(self.board_empty, empty_copy)

    def test_undo_move(self):
        board = self.builder.build_from_moves([1])
        board.undo_move()
        self.assertEqual(self.board_empty, board)

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

        test_board.put_chip(4, 'W')
        expected_board_2 = self.builder.build_from_moves([1,2,4])
        self.assertEqual(expected_board_2, test_board)

        test_board.undo_move()
        self.assertEqual(expected_board_1, test_board)

        test_board = self.builder.build_from_moves([1,2,3,4,5,6,7])
        for _ in range(7):
            test_board.undo_move()
        self.assertEqual(self.board_empty, test_board)

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
        B W W W . . .
        """
        self.assertEquals(getattr(board, winner_method)(), 'W')

        board = self.builder.build_from_moves([7,1,7,7,1,7,2,7,3,7])
        """
        . . . . . . B
        . . . . . . B
        . . . . . . B
        . . . . . . B
        B . . . . . B
        W B B . . . B
        """
        self.assertEquals(getattr(board, winner_method)(), 'B')

    def _test_winner_in_rows(self, winner_method):
        board = self.builder.build_from_moves([1,6,2,6,3,7,4])
        """
        . . . . . . .
        . . . . . . .
        . . . . . . .
        . . . . . . .
        . . . . . W .
        B B B B . W B
        """
        self.assertEquals(getattr(board, winner_method)(), 'W')

        board = self.builder.build_from_moves([7,6,5,4,6,5,4,7,5,4,7,6,5,4,7,6,6,5,4,7,1,7,2,6,1,5,2,4])
        """
        . . . W W W B
        . . . B W B B
        . . . W B W B
        . . . W B W B
        B B . B W B B
        B B . W B W B
        """
        self.assertEquals(getattr(board, winner_method)(), 'B')

    def _test_winner_in_diagonals(self, winner_method):
        board = self.builder.build_from_moves([1,1,1,2,1,2,2,3,3,7,4])
        """
        . . . . . . .
        . . . . . . .
        B . . . . . .
        B B . . . . .
        W W B . . . .
        B W W B . . B
        """
        self.assertEquals(getattr(board, winner_method)(), 'W')

        board = self.builder.build_from_moves([1,1,1,1,1,1,2,3,2,2,2,2,3,3,4,3,4,4])
        """
        W . . . . . .
        B W . . . . .
        W B W . . . .
        B W W W . . .
        W B B B . . .
        B B W B . . .
        """
        self.assertEquals(getattr(board, winner_method)(), 'B')

        board = self.builder.build_from_moves([1,7,6,6,5,4,5,5,4,4,1,4])
        """
        . . . . . . .
        . . . . . . .
        . . . W . . .
        . . . W W . .
        B . . B B W .
        B . . W B B B
        """
        self.assertEquals(getattr(board, winner_method)(), 'B')

        board = self.builder.build_from_moves([7,7,7,6,6,6,6,5,5,5,1,5,5,4,4,4,4,2,4,2,4])
        """
        . . . B . . .
        . . . B B . .
        . . . B W B .
        . . . W W W B
        . W . B B B B
        B W . W W W B
        """
        self.assertEquals(getattr(board, winner_method)(), 'W')

        board = self.builder.build_from_moves([7,7,7,6,7,6,6,5,5,1,4])
        """
        . . . . . . .
        . . . . . . .
        . . . . . . B
        . . . . . B B
        . . . . B W B
        W . . B W W B
        """
        self.assertEquals(getattr(board, winner_method)(), 'W')


        board = self.builder.build_from_moves([7,7,7,7,7,7,6,5,6,6,6,6,5,5,4,5,4,4])
        """
        . . . . . . B
        . . . . . W B
        . . . . W B B
        . . . W W W B
        . . . B B B B
        . . . B W B B
        """
        self.assertEquals(getattr(board, winner_method)(), 'B')

        board = self.builder.build_from_moves([1,1,1,2,2,2,2,3,3,3,7,3,3,4,4,4,4,6,4,6,4])
        """
        . . . B . . .
        . . B B . . .
        . B W B . . .
        B W W W . . .
        W B B B . W .
        B W W W . W B
        """
        self.assertEquals(getattr(board, winner_method)(), 'W')

        board = self.builder.build_from_moves([1,1,1,2,2,2,2,4,4,4,7,4,4,3,3,3,3,6,3,6,4])
        """
        . . . B . . .
        . . B B . . .
        . B B W . . .
        B W W W . . .
        W B B B . W .
        B W W W . W B
        """
        self.assertEquals(getattr(board, winner_method)(), 'W')
