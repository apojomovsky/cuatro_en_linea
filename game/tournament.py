import itertools
from copy import copy
from match import Match
from player import Player
from gameboard import GameBoard

class NotEnoughStrategies(Exception):
    def __init___(self, number_of_strategies):
        self.number_of_strategies = number_of_strategies

class Tournament(object):
    def __init__(self, strategies):
        if len(strategies) < 2:
            raise NotEnoughStrategies(len(strategies))
        self._pairs_of_strategies = list(itertools.permutations(strategies, 2))
        self._number_of_matches = len(self._pairs_of_strategies)
        self._strategies_names = [type(strategy()).__name__ for strategy in strategies]
        self._matches_per_strategy = 2 * (self._number_of_matches - 1)
        self._matches = []
        self._results_table = []
        self.generate_matches()
        self._scores_dict = {}
        for name in self._strategies_names:
            self._scores_dict[name] = 0

    def generate_matches(self):
        for pair_of_strategies in self._pairs_of_strategies:
            board = GameBoard()
            player_one = Player('blue', pair_of_strategies[0]())
            player_two = Player('red', pair_of_strategies[1]())
            self._matches.append(Match(player_one, player_two, board))

    def get_results_table(self):
        return self._results_table

    def get_scores(self):
        return self._scores_dict

    def run(self):
        for match in self._matches:
            match.play_full_match()
            players = match.get_players()
            if match.who_won() is not None:
                self._scores_dict[match.who_won().get_strategy_name()] += 3
                self._results_table.append((
                    players[0].get_strategy_name(),
                    players[1].get_strategy_name(),
                    match.who_won().get_strategy_name()))
            else:
                self._scores_dict[players[0].get_strategy_name()] += 1
                self._scores_dict[players[1].get_strategy_name()] += 1
                self._results_table.append([
                    players[0].get_strategy_name(),
                    players[1].get_strategy_name(),
                    None])
