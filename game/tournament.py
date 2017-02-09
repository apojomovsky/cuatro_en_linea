import itertools
from tabulate import tabulate
from match import Match
from player import Player
from gameboard import GameBoard
from first_non_full_column_strategy import FirstNonFullColumnStrategy
from emptiest_column_strategy import EmptiestColumnStrategy
from closest_to_win_column_strategy import ClosestToWinColumnStrategy

lookup_strategies = {
    'first_non_full_column': FirstNonFullColumnStrategy,
    'emptiest_column': EmptiestColumnStrategy,
    'closest_to_win_column': ClosestToWinColumnStrategy
}

class Tournament(object):
    def __init__(self, strategies):
        self._pairs_of_strategies = itertools.permutations(strategies, 2)
        self.pairs_of_strategies = []
        for pair in self._pairs_of_strategies:
            self.pairs_of_strategies.append(pair)
        self._matches = []
        self._results_table = []
        self.generate_matches()

    def generate_matches(self):
        for pair_of_strategies in self.pairs_of_strategies:
            board = GameBoard()
            player_one = Player('blue', lookup_strategies[pair_of_strategies[0]]())
            player_two = Player('red', lookup_strategies[pair_of_strategies[1]]())
            self._matches.append(Match(player_one, player_two, board))

    def run(self):
        for match in self._matches:
            match.play_full_match()

    def show_results(self):
        for match in self._matches:
            self._results_table.append([match.get_players()[0].get_strategy_name(),
                                 match.get_players()[1].get_strategy_name(),
                                 match.who_won().get_strategy_name()])
        print tabulate(self._results_table, headers=['Player1', 'Player2', 'Winner'])
        self._deliberation()

    def _deliberation(self):
        pass


if __name__ == "__main__":
    tournament = Tournament(lookup_strategies)
    tournament.run()
    tournament.show_results()
