import sys
import argparse
from tournament import Tournament
from tournament import NotEnoughStrategies
from tournament_view import TournamentView
from first_non_full_column_strategy import FirstNonFullColumnStrategy
from emptiest_column_strategy import EmptiestColumnStrategy
from closest_to_win_column_strategy import ClosestToWinColumnStrategy
from random_column_strategy import RandomColumnStrategy

strategies = (
    FirstNonFullColumnStrategy,
    EmptiestColumnStrategy,
    ClosestToWinColumnStrategy,
    RandomColumnStrategy
)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Runs a new tournament of the Connect Four game')
    parser.add_argument('--play-timeout', action='store', dest='play_timeout',
                        default=0.5, help="Time limit for each play")
    parser.add_argument('--prepare-timeout', action='store', dest='prepare_timeout',
                        default=5, help="Time limit for the prepare of each strategy")
    args = parser.parse_args()
    try:
        tournament = Tournament(strategies,
                                prepare_time_limit = args.prepare_timeout,
                                play_time_limit = args.play_timeout)
    except NotEnoughStrategies:
        print "A minimum of 3 strategies is needed to play a tournament"
        sys.exit(1)
    tournament.run()
    tournament_view = TournamentView(tournament)
    tournament_view.show_results_table()
    tournament_view.show_summary()
