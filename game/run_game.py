#!/usr/bin/env python
import argparse
import time
import sys
from match import Match
from gameboard import GameBoard
from gameboard_view import GameBoardView
from player import Player
from strategy_first_non_full_column import StrategyFirstNonFullColumn
from strategy_closest_to_win_column import StrategyClosestToWinColumn
from strategy_emptiest_column import StrategyEmptiestColumn

lookup_strategies = {
    'first_non_full_column': StrategyFirstNonFullColumn,
    'emptiest_column': StrategyEmptiestColumn,
    'closest_to_win_column': StrategyClosestToWinColumn
}

def run(player_one, player_two, rate):
    player_one = Player('blue', lookup_strategies.get(player_one)())
    player_two = Player('red', lookup_strategies.get(player_two)())
    board = GameBoard()
    view = GameBoardView(board)
    match = Match(player_one, player_two, board)
    while not match.is_over():
        match.play_next_turn()
        view.show()
        time.sleep(rate)
    print "Color {} won!".format(match.who_won().color())

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Runs a new match of the Connect Four game')
    parser.add_argument('-p1', '--player-one', action='store', dest='player_one',
                        help="Strategy to be adopted by player one")
    parser.add_argument('-p2', '--player-two', action='store', dest='player_two',
                        help="Strategy to be adopted by player two")
    parser.add_argument('-r', '--rate', action='store', dest='rate',
                        default=2, help="Rate in seconds at which the game will be played")
    args = parser.parse_args()
    if not args.player_one or not args.player_two:
        print "You must provide player_one and player_two strategies as arguments"
        sys.exit(1)
    run(args.player_one, args.player_two, float(args.rate))
