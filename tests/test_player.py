#!/usr/bin/env python
import unittest
from game.player import Player
from game.gameboard import GameBoard
from game.gameboard import ColumnIsFull
from game.gameboard import OutOfIndex
from board_builder import BoardBuilder
from game.emptiest_column_strategy import EmptiestColumnStrategy
from mock import MagicMock

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.strategy_dummy = EmptiestColumnStrategy()
        self.black_player = Player('W', self.strategy_dummy)
        self.builder = BoardBuilder('W', 'B')

    def test_player_play_on_leftmost_column(self):
        self.strategy_dummy.return_column = MagicMock(return_value = 1)
        white_player = Player('W', self.strategy_dummy)
        board = GameBoard() # empty board
        expected_board = self.builder.build_from_moves([1])
        """
        . . . . . . .
        . . . . . . .
        . . . . . . .
        . . . . . . .
        . . . . . . .
        W . . . . . .
        """
        white_player.play(board)
        self.assertEqual(board, expected_board)

    def test_player_play_on_column_in_the_middle(self):
        self.strategy_dummy.return_column = MagicMock(return_value = 4)
        white_player = Player('W', self.strategy_dummy)
        board = GameBoard() # empty board
        expected_board = self.builder.build_from_moves([4])
        """
        . . . . . . .
        . . . . . . .
        . . . . . . .
        . . . . . . .
        . . . . . . .
        . . . W . . .
        """
        white_player.play(board)
        self.assertEqual(board, expected_board)

    def test_player_play_on_rightmost(self):
        self.strategy_dummy.return_column = MagicMock(return_value = 7)
        white_player = Player('W', self.strategy_dummy)
        board = GameBoard() # empty board
        expected_board = self.builder.build_from_moves([7])
        """
        . . . . . . .
        . . . . . . .
        . . . . . . .
        . . . . . . .
        . . . . . . .
        . . . . . . W
        """
        white_player.play(board)
        self.assertEqual(board, expected_board)

    def test_player_play_when_strategy_returns_zero_raises_exception(self):
        self.strategy_dummy.return_column = MagicMock(return_value = 0)
        self.black_player = Player('W', self.strategy_dummy)
        board = GameBoard() # empty board
        with self.assertRaises(OutOfIndex):
            self.black_player.play(board)

    def test_player_play_when_strategy_returns_column_eight_raises_exception(self):
        self.strategy_dummy.return_column = MagicMock(return_value = 8)
        self.black_player = Player('W', self.strategy_dummy)
        board = GameBoard() # empty board
        with self.assertRaises(OutOfIndex):
            self.black_player.play(board)

    def test_player_raises_exception_when_attempts_to_play_on_full_column(self):
        board = self.builder.build_from_moves(
            [1,1,2,2,1,1,2,2,1,1,2,2,4,3,4,4,3,3,4,4,3,
             3,4,3,5,5,5,5,5,5,6,6,6,6,6,6,7,7,7,7,7,7])
        """
        W W W B W W W
        B B W W B B B
        W W B B W W W
        B B W W B B B
        W W B B W W W
        B B W B B B B
        """
        with self.assertRaises(ColumnIsFull):
            self.black_player.play(board)

    def test_player_is_winner_if_it_has_actually_won(self):
        board = self.builder.build_from_moves([1,4,1,5,1,5,1])
        """
        . . . . . . .
        . . . . . . .
        B . . . . . .
        B . . . . . .
        B . . . W . .
        B . . W W . .
        """
        self.assertTrue(self.black_player.is_winner(board))

    def test_player_is_winner_when_has_not_won(self):
        board = self.builder.build_from_moves([1,4,1,5,1,5])
        """
        . . . . . . .
        . . . . . . .
        . . . . . . .
        B . . . . . .
        B . . . W . .
        B . . W W . .
        """
        self.assertFalse(self.black_player.is_winner(board))
