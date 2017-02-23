#!/usr/bin/env python
import unittest
from game.strategy import Strategy
from game.tournament import NotEnoughStrategies
from game.tournament import Tournament
import time
import itertools

class DummyStrategy1(Strategy):
    def return_column(self, board):
        return board.retrieve_first_non_full_column()

class DummyStrategy2(Strategy):
    def return_column(self, board):
        return board.retrieve_first_non_full_column()

    def prepare(self, color, workers_pool):
        time.sleep(0.06)

class DummyStrategy3(Strategy):
    def return_column(self, board):
        time.sleep(0.06)
        return board.retrieve_first_non_full_column()

class DummyStrategy4(DummyStrategy1):
    pass

class TestTournament(unittest.TestCase):
    def test_generate_matches_with_no_strategies(self):
        with self.assertRaises(NotEnoughStrategies):
            strategies = []
            Tournament(strategies)

    def test_generate_matches_with_only_one_strategy(self):
        with self.assertRaises(NotEnoughStrategies):
            strategies = [DummyStrategy1]
            Tournament(strategies)

    def test_generate_matches_with_two_strategies(self):
        with self.assertRaises(NotEnoughStrategies):
            strategies = [DummyStrategy1, DummyStrategy2]
            Tournament(strategies)

    def test_run_with_strategy_that_timeouts_when_playing(self):
        """Ensures that the strategy who violates the play time limits,
           won't win even a single match on the tournament
        """
        strategies = [DummyStrategy1, DummyStrategy4, DummyStrategy3]
        tournament = Tournament(strategies, play_time_limit=0.05)
        tournament.run()
        results = tournament.get_results_table()
        winners = [result[2] for result in results]
        self.assertFalse('DummyStrategy3' in winners)

    def test_run_with_strategy_that_timeouts_when_preparing(self):
        """Ensures that the strategy who violates the prepare time limits,
           won't win even a single match on the tournament
        """
        strategies = [DummyStrategy1, DummyStrategy4, DummyStrategy2]
        tournament = Tournament(strategies, prepare_time_limit=0.05)
        tournament.run()
        results = tournament.get_results_table()
        winners = [result[2] for result in results]
        self.assertFalse('DummyStrategy2' in winners)
