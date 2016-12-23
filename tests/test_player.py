#!/usr/bin/env python
import unittest
from game.player import Player
from game.gameboard import GameBoard

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player_blue = Player('blue')
        self.player_red = Player('red')

    def test_player_with_strategy_one_on_almost_full_board(self):
        board = GameBoard.from_matrix([
                    ['red',  'blue',  'red',  'red', 'blue',   None,  None],
                    ['red',   'red', 'blue',  'red',  'red',   None,  None],
                    ['red',  'blue',  'red',  'red', 'blue', 'blue',  None],
                    ['blue', 'blue',  'red', 'blue',  'red',  'red', 'blue'],
                    ['red',  'blue',  'red', 'blue',  'red', 'blue',  'red'],
                    ['blue',  'red', 'blue',  'red',  'red',  'red',  'red']])
        expected_board = GameBoard.from_matrix([
                    ['red',  'blue',  'red',  'red', 'blue',  'red',  None],
                    ['red',   'red', 'blue',  'red',  'red', 'blue',  None],
                    ['red',  'blue',  'red',  'red', 'blue', 'blue',  None],
                    ['blue', 'blue',  'red', 'blue',  'red',  'red', 'blue'],
                    ['red',  'blue',  'red', 'blue',  'red', 'blue',  'red'],
                    ['blue',  'red', 'blue',  'red',  'red',  'red',  'red']])
        self.player_blue.play(board)
        self.player_red.play(board)
        self.assertEqual(board, expected_board)
