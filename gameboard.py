#!/usr/bin/env python

import sys

class ColumnIsFull(Exception):
    pass

class OutOfIndex(Exception):
    pass

class GameBoard(object):
    ROWSCOUNT = 6
    COLUMNSCOUNT = 7

    def __init__(self):
        self.matrix = self.generate_matrix(self.ROWSCOUNT, self.COLUMNSCOUNT, None)

    def generate_matrix(self, rows, columns, fill):
        return [[fill]*columns for _ in range(rows)]

    def show(self):
        for row in self.matrix:
            for entry in row:
                print '{:4}'.format(entry),
            print
        print

    def retreive_column(self, matrix, columnIndex):
        return reversed([row[columnIndex - 1] for row in matrix])

    def put_chip(self, columnIndex, color):
        try:
            rowIndex = self.ROWSCOUNT - list(self.retreive_column(self.matrix, columnIndex)).index(None) - 1
            self.matrix[rowIndex][columnIndex - 1] = color
        except ValueError:
            raise ColumnIsFull()

    def read_entry(self, rowIndex, columnIndex):
        if rowIndex <= self.ROWSCOUNT and columnIndex <= self.COLUMNSCOUNT:
            entry = self.matrix[self.ROWSCOUNT - rowIndex][columnIndex - 1]
        else:
            raise OutOfIndex()
        return entry


if __name__ == "__main__":
    game = GameBoard()
    game.show()
    game.put_chip(2, 'rojo')
    game.show()
    print game.read_entry(1, 2)
