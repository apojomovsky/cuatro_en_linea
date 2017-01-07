#!/usr/bin/env python
import unittest
from game.player import Player
from game.gameboard import GameBoard
from game.strategy_one import StrategyOne

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player_blue = Player('blue', StrategyOne())
        self.player_red = Player('red', StrategyOne())

    def test_player_with_strategy_one_on_almost_full_board(self):
        board = GameBoard.from_matrix([
                    ['red',  'blue',  'red',  'red', 'blue',   None,   None],
                    ['red',   'red', 'blue',  'red',  'red',   None,   None],
                    ['red',  'blue',  'red',  'red', 'blue', 'blue',   None],
                    ['blue', 'blue',  'red', 'blue',  'red',  'red', 'blue'],
                    ['red',  'blue',  'red', 'blue',  'red', 'blue',  'red'],
                    ['blue',  'red', 'blue',  'red',  'red',  'red',  'red']])
        expected_board = GameBoard.from_matrix([
                    ['red',  'blue',  'red',  'red', 'blue',   None,   None],
                    ['red',   'red', 'blue',  'red',  'red', 'blue',   None],
                    ['red',  'blue',  'red',  'red', 'blue', 'blue',   None],
                    ['blue', 'blue',  'red', 'blue',  'red',  'red', 'blue'],
                    ['red',  'blue',  'red', 'blue',  'red', 'blue',  'red'],
                    ['blue',  'red', 'blue',  'red',  'red',  'red',  'red']])
        self.player_blue.play(board)
        self.assertEqual(board, expected_board)

    def test_player_with_strategy_one_on_second_column(self):
        board = GameBoard.from_matrix([
                    ['red',    None, None, None, None, None, None],
                    ['blue',   None, None, None, None, None, None],
                    ['red',    None, None, None, None, None, None],
                    ['blue',   None, None, None, None, None, None],
                    ['red',   'red', None, None, None, None, None],
                    ['blue', 'blue', None, None, None, None, None]])
        expected_board = GameBoard.from_matrix([
                    ['red',    None, None, None, None, None, None],
                    ['blue',   None, None, None, None, None, None],
                    ['red',    None, None, None, None, None, None],
                    ['blue', 'blue', None, None, None, None, None],
                    ['red',   'red', None, None, None, None, None],
                    ['blue', 'blue', None, None, None, None, None]])
        self.player_blue.play(board)
        self.assertEqual(board, expected_board)

    def test_player_with_strategy_one_blue_not_winning_on_column(self):
        board = GameBoard.from_matrix([
                    [None,     None,   None,   None,  None, None, None],
                    ['blue',   None,   None,   None,  None, None, None],
                    ['red',  'blue',   None, 'blue',  None, None, None],
                    ['blue', 'blue',   None, 'blue',  None, None, None],
                    ['red',  'blue',  'red', 'blue',  None, None, None],
                    ['blue',  'red', 'blue',  'red', 'red', None, None]])
        expected_board = GameBoard.from_matrix([
                    ['blue',   None,   None,   None,  None, None, None],
                    ['blue',   None,   None,   None,  None, None, None],
                    ['red',  'blue',   None, 'blue',  None, None, None],
                    ['blue', 'blue',   None, 'blue',  None, None, None],
                    ['red',  'blue',  'red', 'blue',  None, None, None],
                    ['blue',  'red', 'blue',  'red', 'red', None, None]])
        self.player_blue.play(board)
        self.assertEqual(board, expected_board)

    def test_player_with_strategy_one_red_not_winning_on_row(self):
        board = GameBoard.from_matrix([
                    [None,    None,    None,   None,  None,  None, None],
                    [None,    None,    None,   None,  None,  None, None],
                    [None,    None,    None,   None,  None,  None, None],
                    ['red',   'red',  'red',   None,  None,  None, None],
                    ['blue',  'red', 'blue', 'blue',  None,  None, None],
                    ['blue', 'blue', 'blue',  'red', 'red', 'red', None]])
        expected_board = GameBoard.from_matrix([
                    [None,    None,    None,   None,  None,  None, None],
                    [None,    None,    None,   None,  None,  None, None],
                    ['red',   None,    None,   None,  None,  None, None],
                    ['red',   'red',  'red',   None,  None,  None, None],
                    ['blue',  'red', 'blue', 'blue',  None,  None, None],
                    ['blue', 'blue', 'blue',  'red', 'red', 'red', None]])
        self.player_red.play(board)
        self.assertEqual(board, expected_board)
