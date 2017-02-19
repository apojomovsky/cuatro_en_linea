import sys
from tournament import Tournament
from tournament import NotEnoughStrategies
from tournament_view import TournamentView
from first_non_full_column_strategy import FirstNonFullColumnStrategy
from emptiest_column_strategy import EmptiestColumnStrategy
from closest_to_win_column_strategy import ClosestToWinColumnStrategy

strategies = (
    FirstNonFullColumnStrategy,
    EmptiestColumnStrategy,
    ClosestToWinColumnStrategy
)

if __name__ == "__main__":
    try:
        tournament = Tournament(strategies)
    except NotEnoughStrategies:
        print "A minimum of 2 strategies is needed to play a tournament"
        sys.exit(1)
    tournament.run()
    tournament_view = TournamentView(tournament)
    tournament_view.show_results_table()
    tournament_view.show_summary()
