#!/usr/bin/env python
import unittest
from game.match import Match
from game.match import GameIsOver
from game.player import Player
from game.first_non_full_column_strategy import FirstNonFullColumnStrategy
from game.emptiest_column_strategy import EmptiestColumnStrategy
from game.gameboard import GameBoard
from board_builder import BoardBuilder
from mock import MagicMock

class TestMatch(unittest.TestCase):
    def setUp(self):
        self.strategy_dummy_white = FirstNonFullColumnStrategy()
        self.strategy_dummy_black = EmptiestColumnStrategy()
        self.white_player = Player('W', self.strategy_dummy_white)
        self.black_player = Player('B', self.strategy_dummy_black)
        self.match = Match(self.white_player, self.black_player, GameBoard())
        self.builder = BoardBuilder('W', 'B')

    def get_full_board(self):
        """
        B B W W B W W
        W W B B W B B
        B B W W B W W
        W W B B W B B
        B B W W B W W
        W W B W B B B
        """
        return self.builder.build_from_moves(
            [1,1,2,2,1,1,2,2,1,1,2,2,4,3,4,4,3,3,4,4,3,
             3,4,5,3,5,5,5,5,6,6,6,6,6,6,7,7,7,7,7,7,5])

    def get_almost_full_board(self):
        """
        B B W W . W W
        W W B B W B B
        B B W W B W W
        W W B B W B B
        B B W W B W W
        W W B W B B B
        """
        return self.builder.build_from_moves(
            [1,1,2,2,1,1,2,2,1,1,2,2,4,3,4,4,3,3,4,4,3,
             3,4,5,3,5,5,5,5,6,6,6,6,6,6,7,7,7,7,7,7])

    def test_play_next_turn_on_running_match(self):
        strategy_dummy = EmptiestColumnStrategy()
        strategy_dummy.return_column = MagicMock(return_value = 6)
        white_player = Player('W', strategy_dummy)
        test_board = self.builder.build_from_moves([1,1,1,1,1,2,2,2,3,3,4,3,4,4,5,5,5,2])
        """
        . . . . . . .
        W . . . . . .
        B B . . . . .
        W B B B W . .
        B W B W B . .
        W B W W W . .
        """
        test_match = Match(white_player, self.black_player,
                                         test_board)
        self.assertEqual(test_board.read_entry(1, 6), None)
        test_match.play_next_turn()
        self.assertEqual(test_board.read_entry(1, 6), 'W')

    def test_play_next_turn_after_match_has_finished(self):
        test_board = self.builder.build_from_moves([1,2,1,2,1,2,1])
        """
        . . . . . . .
        . . . . . . .
        W . . . . . .
        W B . . . . .
        W B . . . . .
        W B . . . . .
        """
        test_match = Match(self.white_player, self.black_player,
                                         test_board)
        with self.assertRaises(GameIsOver):
            test_match.play_next_turn()

    def test_play_full_match_with_winner_in_the_end(self):
        self.strategy_dummy_white.return_column = MagicMock(return_value = 1)
        self.strategy_dummy_black.return_column = MagicMock(return_value = 2)
        test_board = GameBoard()
        test_match = Match(self.white_player, self.black_player, test_board)
        self.assertFalse(test_match.is_over())
        test_match.play_full_match()
        """
        . . . . . . .
        . . . . . . .
        W . . . . . .
        W B . . . . .
        W B . . . . .
        W B . . . . .
        """
        self.assertTrue(test_match.is_over)

    def test_play_full_match_with_no_winners_in_the_end(self):
        test_board = self.builder.build_from_moves(
                        [1,1,2,2,1,1,2,2,1,1,2,2,4,3,4,4,3,3,4,4,3,
                         3,4,5,3,5,5,5,5,6,6,6,6,6,6,7,7,7,7,7,7])
        test_match = Match(self.black_player, self.white_player, test_board)
        """
        B B W W . W W
        W W B B W B B
        B B W W B W W
        W W B B W B B
        B B W W B W W
        W W B W B B B
        """
        self.strategy_dummy_black.return_column = MagicMock(return_value = 5)
        test_match.play_full_match()
        self.assertTrue(test_match.is_over())
        self.assertEqual(test_match.who_won(), None)

    def test_who_won_when_valid_winner(self):
        test_board = self.builder.build_from_moves([1,2,1,3,1,3])
        """
        . . . . . . .
        . . . . . . .
        . . . . . . .
        W . . . . . .
        W . B . . . .
        W B B . . . .
        """
        self.strategy_dummy_black.return_column = MagicMock(return_value = 1)
        test_match = Match(self.white_player, self.black_player, test_board)
        self.assertEqual(test_match.who_won(), None)
        test_match.play_next_turn()
        self.assertEqual(test_match.who_won(), self.white_player)
