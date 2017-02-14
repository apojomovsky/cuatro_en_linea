from itertools import cycle
from game.gameboard import GameBoard

class BoardBuilder(object):

    def __init__(self, player_one_color, player_two_color):
        self.player_one_color = player_one_color
        self.player_two_color = player_two_color

    def build_from_moves(self, array_of_moves):
        board = GameBoard()
        color_cycle = cycle([self.player_one_color, self.player_two_color])
        for move in array_of_moves:
            board.put_chip(move, color_cycle.next())
        return board


