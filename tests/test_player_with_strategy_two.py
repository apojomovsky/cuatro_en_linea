#!/usr/bin/env python
import unittest
from game.player_with_strategy_two import PlayerWithStrategyTwo
from game.gameboard import GameBoard

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player_blue = PlayerWithStrategyTwo('blue')
        self.player_red = PlayerWithStrategyTwo('red')

    def test_player_with_strategy_two_on_almost_full_board(self):
        board = GameBoard.from_matrix([
                    ['red',    None,   None,   None,   None,   None,   None],
                    ['red',   'red', 'blue',  'red',  'red',  'red',   None],
                    ['red',  'blue',  'red',  'red', 'blue', 'blue', 'blue'],
                    ['blue', 'blue',  'red', 'blue',  'red', 'blue',  'red'],
                    ['red',  'blue',  'red', 'blue',  'red', 'blue', 'blue'],
                    ['blue',  'red', 'blue',  'red',  'red',  'red',  'red']])
        expected_board = GameBoard.from_matrix([
                    ['red',   'red',   None,   None,   None,   None,   None],
                    ['red',   'red', 'blue',  'red',  'red',  'red', 'blue'],
                    ['red',  'blue',  'red',  'red', 'blue', 'blue', 'blue'],
                    ['blue', 'blue',  'red', 'blue',  'red', 'blue',  'red'],
                    ['red',  'blue',  'red', 'blue',  'red', 'blue', 'blue'],
                    ['blue',  'red', 'blue',  'red',  'red',  'red',  'red']])
        self.player_blue.play(board)
        self.player_red.play(board)
        self.assertEqual(board, expected_board)

    def test_player_with_strategy_two_on_semi_empty_board(self):
        board = GameBoard.from_matrix([
                    [None,    None,   None,   None,  None, None,   None],
                    [None,    None,   None,   None,  None, None,   None],
                    [None,    None,   None,   None,  None, None,   None],
                    [None,    None,   None,   None,  None, None,   None],
                    [None,  'blue',   None, 'blue',  None, None, 'blue'],
                    ['red', 'blue', 'blue', 'blue', 'red', None,  'red']])
        expected_board = GameBoard.from_matrix([
                    [None,    None,   None,   None,  None, None,   None],
                    [None,    None,   None,   None,  None, None,   None],
                    [None,    None,   None,   None,  None, None,   None],
                    [None,    None,   None,   None,  None, None,   None],
                    ['red',  'blue',   None, 'blue',  None, None, 'blue'],
                    ['red', 'blue', 'blue', 'blue', 'red', 'blue',  'red']])
        self.player_blue.play(board)
        self.player_red.play(board)
        self.assertEqual(board, expected_board)

    def test_player_with_strategy_two_red_not_winning_on_column(self):
        board = GameBoard.from_matrix([
                    ['red',    None,   None,   None,    None,   None,   None],
                    ['blue',   None,   None,   None,    None,   None,   None],
                    ['blue',   None,  'red',  'red',  'blue', 'blue', 'blue'],
                    ['blue', 'blue',  'red',  'red',   'red', 'blue', 'blue'],
                    ['red',  'blue',  'red',  'red',  'blue', 'blue', 'blue'],
                    ['blue',  'red', 'blue',  'blue', 'blue',  'red',  'red']])
        expected_board = GameBoard.from_matrix([
                    ['red',    None,   None,   None,    None,   None,   None],
                    ['blue', 'blue',   None,   None,    None,   None,   None],
                    ['blue',  'red',  'red',  'red',  'blue', 'blue', 'blue'],
                    ['blue', 'blue',  'red',  'red',   'red', 'blue', 'blue'],
                    ['red',  'blue',  'red',  'red',  'blue', 'blue', 'blue'],
                    ['blue',  'red', 'blue',  'blue', 'blue',  'red',  'red']])
        self.player_red.play(board)
        self.player_blue.play(board)
        self.assertEqual(board, expected_board)

    def test_player_with_strategy_two_red_not_winning_on_row(self):
        board = GameBoard.from_matrix([
                    [None,    None,   None,   None,   None,   None,   None],
                    [None,    None,   None,  'red',  'red',  'red',   None],
                    [None,    None,  'red',  'red',  'red', 'blue', 'blue'],
                    [None,  'blue',  'red', 'blue',  'blue', 'red', 'blue'],
                    ['red', 'blue',  'red', 'blue',  'red', 'blue', 'blue'],
                    ['blue', 'red', 'blue',  'red',  'red',  'red',  'red']])
        expected_board = GameBoard.from_matrix([
                    [None,    None,   None,   None,   None,   None,   None],
                    [None,    None,   None,  'red',  'red',  'red',   None],
                    ['blue',  None,  'red',  'red',  'red', 'blue', 'blue'],
                    ['red', 'blue',  'red', 'blue',  'blue', 'red', 'blue'],
                    ['red', 'blue',  'red', 'blue',  'red', 'blue', 'blue'],
                    ['blue', 'red', 'blue',  'red',  'red',  'red',  'red']])
        self.player_red.play(board)
        self.player_blue.play(board)
        self.assertEqual(board, expected_board)
