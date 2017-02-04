#!/usr/bin/env python
import unittest
from game.player import Player
from game.gameboard import GameBoard
from game.gameboard import BoardIsFull
from game.gameboard import OutOfIndex
from game.strategy_one import StrategyOne
from mock import MagicMock

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.strategy_dummy = StrategyOne()
        self.strategy_dummy.return_column = MagicMock(return_value = 1)
        self.player_blue = Player('blue', self.strategy_dummy)

    def test_player_play_on_leftmost_column(self):
        self.strategy_dummy.return_column = MagicMock(return_value = 1)
        self.player_blue = Player('blue', self.strategy_dummy)
        board = GameBoard() # empty board
        expected_board = GameBoard.from_matrix([
                    [None,   None, None, None, None, None, None],
                    [None,   None, None, None, None, None, None],
                    [None,   None, None, None, None, None, None],
                    [None,   None, None, None, None, None, None],
                    [None,   None, None, None, None, None, None],
                    ['blue', None, None, None, None, None, None]])
        self.player_blue.play(board)
        self.assertEqual(board, expected_board)

    def test_player_play_on_column_in_the_middle(self):
        self.strategy_dummy.return_column = MagicMock(return_value = 4)
        self.player_blue = Player('blue', self.strategy_dummy)
        board = GameBoard() # empty board
        expected_board = GameBoard.from_matrix([
                    [None, None, None, None,   None, None, None],
                    [None, None, None, None,   None, None, None],
                    [None, None, None, None,   None, None, None],
                    [None, None, None, None,   None, None, None],
                    [None, None, None, None,   None, None, None],
                    [None, None, None, 'blue', None, None, None]])
        self.player_blue.play(board)
        self.assertEqual(board, expected_board)

    def test_player_play_on_rightmost(self):
        self.strategy_dummy.return_column = MagicMock(return_value = 7)
        self.player_blue = Player('blue', self.strategy_dummy)
        board = GameBoard() # empty board
        expected_board = GameBoard.from_matrix([
                    [None, None, None, None, None, None,   None],
                    [None, None, None, None, None, None,   None],
                    [None, None, None, None, None, None,   None],
                    [None, None, None, None, None, None,   None],
                    [None, None, None, None, None, None,   None],
                    [None, None, None, None, None, None, 'blue']])
        self.player_blue.play(board)
        self.assertEqual(board, expected_board)

    def test_player_play_when_strategy_returns_zero_raises_exception(self):
        self.strategy_dummy.return_column = MagicMock(return_value = 0)
        self.player_blue = Player('blue', self.strategy_dummy)
        board = GameBoard() # empty board
        with self.assertRaises(OutOfIndex):
            self.player_blue.play(board)

    def test_player_play_when_strategy_returns_column_eight_raises_exception(self):
        self.strategy_dummy.return_column = MagicMock(return_value = 8)
        self.player_blue = Player('blue', self.strategy_dummy)
        board = GameBoard() # empty board
        with self.assertRaises(OutOfIndex):
            self.player_blue.play(board)

    def test_player_raises_exception_when_attempts_to_play_on_full_board(self):
        board = GameBoard.from_matrix([
                    ['red',  'blue',  'red',  'red', 'blue', 'blue',  'red'],
                    ['red',   'red', 'blue',  'red',  'red', 'blue',  'red'],
                    ['red',  'blue',  'red',  'red', 'blue', 'blue', 'blue'],
                    ['blue', 'blue',  'red', 'blue',  'red',  'red', 'blue'],
                    ['red',  'blue',  'red', 'blue',  'red', 'blue',  'red'],
                    ['blue',  'red', 'blue',  'red',  'red',  'red',  'red']])
        with self.assertRaises(BoardIsFull):
            self.player_blue.play(board)

    def test_player_is_winner_if_it_has_actually_won(self):
        board = GameBoard.from_matrix([
                    [None,   None, None,  None,  None, None, None],
                    [None,   None, None,  None,  None, None, None],
                    ['blue', None, None,  None,  None, None, None],
                    ['blue', None, None,  None,  None, None, None],
                    ['blue', None, None,  None, 'red', None, None],
                    ['blue', None, None, 'red', 'red', None, None]])
        self.assertTrue(self.player_blue.is_winner(board))

    def test_player_is_winner_when_has_not_won(self):
        board = GameBoard.from_matrix([
                    [None,   None, None,  None,  None, None, None],
                    [None,   None, None,  None,  None, None, None],
                    [None,   None, None,  None,  None, None, None],
                    ['blue', None, None,  None,  None, None, None],
                    ['blue', None, None,  None, 'red', None, None],
                    ['blue', None, None, 'red', 'red', None, None]])
        self.assertFalse(self.player_blue.is_winner(board))
