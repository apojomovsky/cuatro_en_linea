#!/usr/bin/env python
import unittest
from game.match import Match
from game.player import Player
from game.player import GameBoard


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.board = GameBoard()
        self.player_blue = Player('blue')
        self.player_red = Player('red')

        self.board_player_blue_wins = GameBoard.from_matrix([
                    [None,     None,  None,   None,   None,   None,   None],
                    [None,     None,  None,   None,   None,   None,   None],
                    ['blue',   None,  None,   None,   None,   None,   None],
                    ['blue',   None,  None,   None, 'blue',  'red', 'blue'],
                    ['blue', 'blue',  None, 'blue',  'red', 'blue',  'red'],
                    ['red',   'red', 'red',  'red',  'red', 'blue',  'red']])

        self.board_player_red_wins = GameBoard.from_matrix([
                    [None,     None,   None,  None,  None,   None,   None],
                    [None,     None,   None,  None,  None,   None,   None],
                    [None,     None,   None,  None,  None,   None,  'red'],
                    ['blue', 'blue',  'red',  None,  None,   None,  'red'],
                    ['blue',  'red',  'red', 'red',  None,  'blue', 'red'],
                    ['red',  'blue', 'blue', 'red', 'blue', 'blue', 'blue']])

    def test_is_winner(self):
        self.assertFalse(self.player_blue.is_winner(self.board_player_blue_wins))
        self.player_blue.play_on_emptiest_column(self.board_player_blue_wins)
        self.assertTrue(self.player_blue.is_winner(self.board_player_blue_wins))


    def test_play_on_first_non_full_column_left_to_right(self):
        self.assertFalse(self.player_blue.is_winner(self.board_player_blue_wins))
        self.player_blue.play_on_first_non_full_column(self.board_player_blue_wins)
        self.assertTrue(self.player_blue.is_winner(self.board_player_blue_wins))

    def test_play_on_first_non_full_column_right_to_left(self):
        self.assertFalse(self.player_red.is_winner(self.board_player_red_wins))
        self.player_red.play_on_first_non_full_column(self.board_player_red_wins, True)
        self.assertTrue(self.player_red.is_winner(self.board_player_red_wins))

    def test_play_on_emptiest_column_left_to_right(self):
        self.assertFalse(self.player_blue.is_winner(self.board_player_blue_wins))
        self.player_blue.play_on_emptiest_column(self.board_player_blue_wins)
        self.assertTrue(self.player_blue.is_winner(self.board_player_blue_wins))

    def test_play_on_emptiest_column_right_to_left(self):
        self.assertFalse(self.player_red.is_winner(self.board_player_red_wins))
        self.player_red.play_on_emptiest_column(self.board_player_red_wins, True)
        self.assertTrue(self.player_red.is_winner(self.board_player_red_wins))
