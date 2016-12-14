#!/usr/bin/env python
import unittest
from game.player import PlayerWithStrategyTwo
from game.player import GameBoard

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player_blue = PlayerWithStrategyTwo('blue')
        self.player_red = PlayerWithStrategyTwo('red')

    def test_player_with_strategy_two_blue_wins_on_right_almost_upper_corner(self):
        board = GameBoard.from_matrix([
                    ['red',    None,   None,   None,   None,   None,   None],
                    ['red',   'red', 'blue',  'red',  'red',  'red',   None],
                    ['red',  'blue',  'red',  'red', 'blue', 'blue', 'blue'],
                    ['blue', 'blue',  'red', 'blue',  'red', 'blue', 'blue'],
                    ['red',  'blue',  'red', 'blue',  'red', 'blue', 'blue'],
                    ['blue',  'red', 'blue',  'red',  'red',  'red',  'red']])
        self.assertFalse(self.player_blue.is_winner(board))
        self.player_blue.play(board)
        self.assertTrue(self.player_blue.is_winner(board))


    def test_player_with_strategy_two_blue_wins_on_left_lower_corner(self):
        board = GameBoard.from_matrix([
                    [None,   None,   None,   None,  None, None,   None],
                    [None,   None,   None,   None,  None, None,   None],
                    [None,   None,   None,   None,  None, None, 'red'],
                    [None,  'red',   None,   None,  None, None, 'blue'],
                    [None, 'blue',   None, 'blue',  None, None, 'blue'],
                    [None, 'blue', 'blue', 'blue',  None, None,  'red']])
        self.assertFalse(self.player_blue.is_winner(board))
        self.player_blue.play(board)
        self.assertTrue(self.player_blue.is_winner(board))

    '''
    def test_player_with_strategy_two_blue_wins_on_left_corner(self):
        self.board = GameBoard.from_matrix([
                    [None,    None,    None,  None, 'blue',  'blue',   None],
                    ['blue',   None,   None,  'red',  'red',  'red', 'blue'],
                    ['blue', 'blue',   None,  'red', 'blue', 'blue', 'blue'],
                    ['blue', 'blue',  'red', 'blue',  'red', 'blue', 'blue'],
                    ['red',  'blue',  'red', 'blue',  'red', 'blue',  'red'],
                    ['blue',  'red', 'blue',  'red',  'red',  'red',  'red']])
        self.assertFalse(self.player_blue.is_winner(self.board))
        self.player_blue.play(self.board)
        self.assertTrue(self.player_blue.is_winner(self.board))

    def test_player_with_strategy_two_red_not_winning_on_column(self):
        self.board = GameBoard.from_matrix([
                    [None,     None,   None,   None,  None, None, None],
                    [None,     None,   None,   None,  None, None, None],
                    ['red',  'blue',   None, 'blue',  None, None, None],
                    ['blue', 'blue',   None, 'blue',  None, None, None],
                    ['red',  'blue',  'red', 'blue',  None, None, None],
                    ['blue',  'red', 'blue',  'red', 'red', None, None]])
        self.assertFalse(self.player_blue.is_winner(self.board))
        self.player_blue.play(self.board)
        self.assertFalse(self.player_blue.is_winner(self.board))

    def test_player_with_strategy_two_red_not_winning_on_row(self):
        self.board = GameBoard.from_matrix([
                    [None,    None,    None,   None,  None,  None, None],
                    [None,    None,    None,   None,  None,  None, None],
                    [None,    None,    None,   None,  None,  None, None],
                    ['red',   'red',  'red',   None,  None,  None, None],
                    ['blue', 'blue', 'blue', 'blue',  None,  None, None],
                    ['blue', 'blue', 'blue',  'red', 'red', 'red', None]])
        self.assertFalse(self.player_red.is_winner(self.board))
        self.player_red.play(self.board)
        self.assertFalse(self.player_red.is_winner(self.board))
    '''
