
#!/usr/bin/env python
from match import Match
from gameboard import GameBoard
from player import Player
from strategy_one import StrategyOne
from strategy_two import StrategyTwo
import time
import sys

print sys.path

if __name__ == "__main__":
    player_one = Player('blue', StrategyOne())
    player_two = Player('red', StrategyTwo())
    board = GameBoard()
    match = Match(player_one, player_two, board)
    while not match.is_over():
        print(chr(27) + "[2J")
        match.play_next_turn()
        board.show()
        time.sleep(1)
    print "Color {} won!".format(match.who_won().color())
