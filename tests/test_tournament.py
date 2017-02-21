#!/usr/bin/env python
import unittest
from game.tournament import NotEnoughStrategies
from game.tournament import Tournament
from game.emptiest_column_strategy import EmptiestColumnStrategy
from mock import MagicMock


class TestTournament(unittest.TestCase):
    def setUp(self):
        self.strategy_dummy_first = EmptiestColumnStrategy()
        self.strategy_dummy_first.return_column = MagicMock(return_value = 1)
        self.strategy_dummy_second = EmptiestColumnStrategy()
        self.strategy_dummy_second.return_column = MagicMock(return_value = 2)

    def test_generate_matches_with_no_strategies(self):
        with self.assertRaises(NotEnoughStrategies):
            list_of_strategies = []
            Tournament(list_of_strategies)

    def test_generate_matches_with_only_one_strategy(self):
        with self.assertRaises(NotEnoughStrategies):
            list_of_strategies = [EmptiestColumnStrategy]
            Tournament(list_of_strategies)

    def test_generate_matches_with_two_strategies(self):
        list_of_strategies = [EmptiestColumnStrategy, EmptiestColumnStrategy]
        Tournament(list_of_strategies)

    #def test_run_
