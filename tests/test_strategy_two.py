#!/usr/bin/env python
import unittest
from game.gameboard import GameBoard
from game.gameboard import BoardIsFull
from game.strategy_two import StrategyTwo

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.strategy_two = StrategyTwo()
        self.color = 'blue'


    def test_strategy_two_choses_emptiest_rightmost_column(self):
        board = GameBoard.from_matrix([
                    [None,    None,   None,   None,  None, None,   None],
                    [None,    None,   None,   None,  None, None,   None],
                    [None,    None,   None,   None,  None, None,   None],
                    [None,    None,   None,   None,  None, None,   None],
                    [None,    None,   None,   None,  None, None,   None],
                    ['red', 'blue', 'blue', 'blue', 'red', 'blue', None]])
        self.assertEqual(self.strategy_two.return_column(board), 7)

    def test_strategy_two_choses_emptiest_rightmost_column(self):
        board = GameBoard.from_matrix([
                    [None,    None,   None,   None,  None, None,   None],
                    [None,    None,   None,   None,  None, None,   None],
                    [None,    None,   None,   None,  None, None,   None],
                    [None,    None,   None,   None,  None, None,   None],
                    [None,    None,   None,   None,  None, None,   None],
                    ['red', 'blue', 'blue', 'blue', 'red', 'blue', None]])
        self.assertEqual(self.strategy_two.return_column(board), 7)

    def test_strategy_two_choses_emptiest_leftmost_column(self):
        board = GameBoard.from_matrix([
                    [None,   None,   None,   None,  None,   None,  None],
                    [None,   None,   None,   None,  None,   None,  None],
                    [None,   None,   None,   None,  None,   None,  None],
                    [None,   None,   None,   None,  None,   None,  None],
                    [None,   None,   None,   None,  None,   None,  None],
                    [None, 'blue', 'blue', 'blue', 'red', 'blue', 'red']])
        self.assertEqual(self.strategy_two.return_column(board), 1)

    def test_strategy_two_choses_leftmost_empty_when_more_than_one_equally_empty(self):
        board = GameBoard.from_matrix([
                    [None,     None, None,  None,  None,   None,   None],
                    [None,     None, None,  None,  None,   None,   None],
                    [None,     None, None,  None,  None,   None,   None],
                    [None,     None, None,  None,  None,   None,   None],
                    ['red',  'blue', None,  None, 'blue', 'red', 'blue'],
                    ['blue',  'red', 'red', 'red', 'red', 'blue', 'red']])
        self.assertEqual(self.strategy_two.return_column(board), 3)

    def test_strategy_two_choses_emptiests_column_from_mid_loaded_board(self):
        board = GameBoard.from_matrix([
                    [None,    None,   None,   None,   None,   None,   None],
                    [None,    None,   None,   None,   None,   None,   None],
                    [None,    None,   None,   None,   None,   None,   None],
                    ['red', 'blue',  'red',   None,  'red', 'blue', 'blue'],
                    ['red', 'blue',  'red',  'red', 'blue', 'blue', 'blue'],
                    ['blue', 'red', 'blue', 'blue', 'blue',  'red',  'red']])
        self.assertEqual(self.strategy_two.return_column(board), 4)

    def test_strategy_two_choses_leftmost_column_on_empty_board(self):
        board = GameBoard()
        self.assertEqual(self.strategy_two.return_column(board), 1)

    def test_strategy_two_raises_exception_when_board_is_full(self):
        board = GameBoard.from_matrix([
                    ['red',  'blue',  'red',  'red', 'blue', 'blue', 'blue'],
                    ['red',   'red', 'blue',  'red', 'blue',  'red',  'red'],
                    ['red',  'blue',  'red',  'red', 'blue', 'blue', 'blue'],
                    ['blue', 'blue',  'red', 'blue',  'red',  'red', 'blue'],
                    ['red',  'blue',  'red', 'blue',  'red', 'blue',  'red'],
                    ['blue',  'red', 'blue',  'red',  'red',  'red',  'red']])
        with self.assertRaises(BoardIsFull):
            self.strategy_two.return_column(board)
