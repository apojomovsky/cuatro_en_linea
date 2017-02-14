import itertools
from copy import copy
from match import Match
from player import Player
from gameboard import GameBoard


class Tournament(object):
    def __init__(self, strategies):
        self._pairs_of_strategies = itertools.permutations(strategies, 2)
        self._number_of_matches = len([1 for i in self._pairs_of_strategies])
        self._pairs_of_strategies = itertools.permutations(strategies, 2)
        self._strategies_names = [type(strategy()).__name__ for strategy in strategies]
        self._matches_per_strategy = 2 * (self._number_of_matches - 1)
        self._matches = []
        self._results_table = []
        self.generate_matches()
        self.scores_dict = {}
        for name in self._strategies_names:
            self.scores_dict[name] = 0
        print self.scores_dict

    def generate_matches(self):
        for pair_of_strategies in self._pairs_of_strategies:
            board = GameBoard()
            player_one = Player('blue', pair_of_strategies[0]())
            player_two = Player('red', pair_of_strategies[1]())
            self._matches.append(Match(player_one, player_two, board))

    def results_table(self):
        return copy(self._results_table)

    def scores(self):
        return copy(self.scores_dict)

    def run(self):
        for match in self._matches:
            match.play_full_match()
            if match.who_won() is not None:
                self.scores_dict[match.who_won().get_strategy_name()] += 3
                self._results_table.append([
                    match.get_players()[0].get_strategy_name(),
                    match.get_players()[1].get_strategy_name(),
                    match.who_won().get_strategy_name()])
            else:
                self.scores_dict[match.get_players()[0].get_strategy_name()] += 1
                self.scores_dict[match.get_players()[1].get_strategy_name()] += 1
                self._results_table.append([
                    match.get_players()[0].get_strategy_name(),
                    match.get_players()[1].get_strategy_name(),
                    None])
