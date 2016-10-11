#!/usr/bin/env python
import unittest
from game.match import Match
from game.player import Player

class TestMatch(unittest.TestCase):
    def setUp(self):
        self.match = Match(Player('red'), Player('blue'))
        self.match_red_win_with_row_ = Match(Player('red'), Player('blue'), GameBoard.from_matrix([
                    [None,   'red',  'red',  'red',   None,   None, None],
                    ['red', 'blue',  'red', 'blue',   None,   None, None],
                    ['blue', 'red', 'blue',  'red',   None,   None, None],
                    ['blue', 'red',  'red', 'blue',   None,   None, None],
                    ['red', 'blue',  'red', 'blue',   None,   None, None],
                    ['blue', 'red', 'blue',  'red',  'red',  'red', None]]))

        self.match_blue_win_with_column = Match(Player('red'), Player('blue'), GameBoard.from_matrix([
                    [None,   None, None, None, None, None,   None],
                    ['blue', None, None, None, None, None, 'blue'],
                    ['blue', None, None, None, None, None, 'blue'],
                    ['blue', None, None, None, None, None, 'blue'],
                    ['red',  None, None, None, None, None,  'red'],
                    ['red',  None, None, None, None, None,  'red']]))

        self.match_with_mid_full_board = Match(Player('red'), Player('blue'), GameBoard.from_matrix([
                    [None,     None,   None,   None,   None,   None,   None],
                    ['red',   'red',   None,   None,   None,  'red', 'blue'],
                    ['blue', 'blue',  'red',   None,  'red', 'blue',  'red'],
                    ['red',  'blue',  'red',  'red',  'red', 'blue', 'blue'],
                    ['blue',  'red', 'blue', 'blue', 'blue',  'red',  'red'],
                    ['red',  'blue', 'blue',  'red', 'blue',  'red', 'blue']]))

    '''
    def test_play_next_turn_on_running_match(self):
        self.match_with_mid_full_board.play_next_turn()
        self.board.put_chip(3, 'red')
        self.assertEqual(self.board.read_entry(1, 3), 'red')

    def test_play_next_turn_after_match_has_finished(self):
        pass

    def test_play_match_when_red_should_win(self):
        pass

    def test_play_match_when_blue_should_win(self):
        pass

    def test_who_won_when_winner(self):
        pass

    def test_who_won_when_no_winner(self):
        pass
    '''
