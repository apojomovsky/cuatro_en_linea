from tournament import Tournament
from tabulate import tabulate

class TournamentView(object):
    def __init__(self, tournament):
        self._tournament = tournament

    def show_results_table(self):
        print "Results table:"
        print tabulate(self._tournament.get_results_table(),
                       headers=['Player1', 'Player2', 'Winner'])

    def show_summary(self):
        print "\nScores:"
        scores = self._tournament.get_scores()
        for strategy in scores:
            print "{0}: {1}".format(strategy, scores[strategy])
        highest = max(scores.values())
        winners_list = [strategy_name for strategy_name, score in scores.items() if score == highest]
        if len(winners_list) > 1:
            print "\nThere was a tie between {0} strategies: {1}".format(len(winners_list), winners_list)
        else:
            print "The winner of the tournament is: {0}, with {1} points".format(winners_list[0], scores[winners_list[0]])
