#!/usr/bin/env python
import unittest
from game.player import Player
from game.gameboard import GameBoard
from game.strategy_three import StrategyThree

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player_blue = Player.with_strategy('blue', StrategyThree())
        self.player_red = Player.with_strategy('red', StrategyThree())

    def test_strategy_three_red_wins_on_third_column(self):
        board = GameBoard.from_matrix([
                    ['red',    None,   None,   None,   None,   None,   None],
                    ['blue',   None,   None,   None,   None,   None,   None],
                    ['blue',   None,  'red',  'red', 'blue', 'blue', 'blue'],
                    ['blue', 'blue',  'red', 'blue',  'red', 'blue', 'blue'],
                    ['red',  'blue',  'red',  'red', 'blue', 'blue', 'blue'],
                    ['blue',  'red', 'blue', 'blue', 'blue',  'red',  'red']])
        expected_board = GameBoard.from_matrix([
                    ['red',    None,   None,   None,   None,   None,   None],
                    ['blue',   None,  'red',   None,   None,   None,   None],
                    ['blue',   None,  'red',  'red', 'blue', 'blue', 'blue'],
                    ['blue', 'blue',  'red', 'blue',  'red', 'blue', 'blue'],
                    ['red',  'blue',  'red',  'red', 'blue', 'blue', 'blue'],
                    ['blue',  'red', 'blue', 'blue', 'blue',  'red',  'red']])
        self.player_red.play(board)
        self.assertEqual(board, expected_board)

    def test_strategy_three_red_plays_on_third_column_cannot_win_on_first(self):
        board = GameBoard.from_matrix([
                    [None,   None, None, None, None, None,   None],
                    ['blue', None, None, None, None, None,   None],
                    ['blue', None, None, None, None, None,   None],
                    ['red',  None, None, None, None, None, 'blue'],
                    ['red',  None, None, None, None, None,  'red'],
                    ['red',  None, None, None, None, None,  'red']])

        expected_board = GameBoard.from_matrix([
                    [None,   None, None, None, None, None,   None],
                    ['blue', None, None, None, None, None,   None],
                    ['blue', None, None, None, None, None, 'blue'],
                    ['red',  None, None, None, None, None, 'blue'],
                    ['red',  None, None, None, None, None,  'red'],
                    ['red',  None, None, None, None, None,  'red']])
        self.player_blue.play(board)
        self.assertEqual(board, expected_board)
