import random
import sys
sys.path.append('..')

from game.gameboard import GameBoard
from board_builder import BoardBuilder

class RandomBoardsGenerator(object):
    def __init__(self, number_of_moves=42, color_one='red', color_two='blue'):
        self._number_of_moves = number_of_moves
        self._color_one = color_one
        self._color_two = color_two
        self._moves = [1,1,1,1,1,1,
                       2,2,2,2,2,2,
                       3,3,3,3,3,3,
                       4,4,4,4,4,4,
                       5,5,5,5,5,5,
                       6,6,6,6,6,6,
                       7,7,7,7,7,7]
        self._selected_moves = None

    def generate(self):
        builder = BoardBuilder(self._color_one, self._color_two)
        while True:
            moves = self._moves
            random.shuffle(moves)
            test_board = None
            try:
                moves = moves[:self._number_of_moves]
                test_board = builder.build_from_moves(moves)
            except Exception:
                pass
            if test_board is not None:
                if not test_board.winner_exists():
                    self._selected_moves = moves
                    return test_board

    def show_moves(self):
        return self._selected_moves


if __name__ == "__main__":
    generator = RandomBoardsGenerator(42)
    print generator.generate()
    print generator.show_moves()
