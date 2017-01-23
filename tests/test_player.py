#!/usr/bin/env python
import unittest
from game.player import Player
from game.gameboard import GameBoard
from game.strategy_one import StrategyOne
from mock import MagicMock

class TestPlayer(unittest.TestCase):
    def setUp(self):
        strategy_dummy = StrategyOne()
        strategy_dummy.return_column = MagicMock(return_value = 1)
        self.player_blue = Player('blue', strategy_dummy)

    def test_player_play_with_dummy_strategy(self):
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

    def test_player_is_winner_when_is_true(self):
        board = GameBoard.from_matrix([
                    [None,   None, None,  None,  None, None, None],
                    [None,   None, None,  None,  None, None, None],
                    ['blue', None, None,  None,  None, None, None],
                    ['blue', None, None,  None,  None, None, None],
                    ['blue', None, None,  None, 'red', None, None],
                    ['blue', None, None, 'red', 'red', None, None]])
        self.assertTrue(self.player_blue.is_winner(board))

    def test_player_is_winner_when_is_false(self):
        board = GameBoard.from_matrix([
                    [None,   None, None,  None,  None, None, None],
                    [None,   None, None,  None,  None, None, None],
                    [None,   None, None,  None,  None, None, None],
                    ['blue', None, None,  None,  None, None, None],
                    ['blue', None, None,  None, 'red', None, None],
                    ['blue', None, None, 'red', 'red', None, None]])
        self.assertFalse(self.player_blue.is_winner(board))
