from gameboard import GameBoard
import time

class Match(object):
    def __init__(self):
        self.game = GameBoard()
        self.start_time = time.time()
        self.is_running = True
        self.active_player = 'blue'

    def elapsed_time(self):
        return time.time() - self.start_time()

    def next_turn(self):
        if self.active_player == 'blue':
            self.active_player = 'red'
        else:
            self.active_player = 'blue'
        return self.active_player

    def automatic_playing(self):
        for column in range(1, 8):
            while self.game.read_entry(6, column) == '-':
                if not self.game.winner_exists():
                    self.game.put_chip(column, self.active_player)
                    self.game.show()
                    self.next_turn()
                else:
                    return True
        return False
