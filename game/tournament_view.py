from tournament import Tournament
from tabulate import tabulate

class TournamentView(object):
    def __init__(self, tournament):
        self._tournament = tournament

    def show_results_table(self):
        print tabulate(self._tournament.get_results_table(),
                       headers=['Player1', 'Player2', 'Winner'])

    def show_statistics(self):
        print "\nScores:"
        scores = self._tournament.get_scores()
        for strategy in scores:
            print "{0}: {1}".format(strategy, scores[strategy])
