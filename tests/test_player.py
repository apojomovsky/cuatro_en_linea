#!/usr/bin/env python
import unittest
from game.player import Player
from game.gameboard import GameBoard

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player_blue = Player('blue')
        self.player_red = Player('red')

    def test_player_with_default_strategy(self):
        board = GameBoard.from_matrix([
                    ['red',  'blue',  'red',  'red', 'blue',   None,  None],
                    ['red',   'red', 'blue',  'red',  'red',   None,  None],
                    ['red',  'blue',  'red',  'red', 'blue', 'blue',  None],
                    ['blue', 'blue',  'red', 'blue',  'red',  'red', 'blue'],
                    ['red',  'blue',  'red', 'blue',  'red', 'blue',  'red'],
                    ['blue',  'red', 'blue',  'red',  'red',  'red',  'red']])
        expected_board = GameBoard.from_matrix([
                    ['red',  'blue',  'red',  'red', 'blue',   None,  None],
                    ['red',   'red', 'blue',  'red',  'red', 'blue',  None],
                    ['red',  'blue',  'red',  'red', 'blue', 'blue',  None],
                    ['blue', 'blue',  'red', 'blue',  'red',  'red', 'blue'],
                    ['red',  'blue',  'red', 'blue',  'red', 'blue',  'red'],
                    ['blue',  'red', 'blue',  'red',  'red',  'red',  'red']])
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
