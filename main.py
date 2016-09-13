#!/usr/bin/env python

import sys

class ColumnIsFull(Exception):
    pass

class OutOfIndex(Exception):
    pass

class GameBoard(object):
    rowsCount = 6
    columnsCount = 7

    def __init__(self):
        self.matrix = self.generate_matrix(self.rowsCount, self.columnsCount, None)

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
            rowIndex = self.rowsCount - list(self.retreive_column(self.matrix, columnIndex)).index(None) - 1
            self.matrix[rowIndex][columnIndex - 1] = color
        except ValueError:
            raise ColumnIsFull()

    def read_entry(self, rowIndex, columnIndex):
        if rowIndex <= self.rowsCount and columnIndex <= self.columnsCount:
            entry = self.matrix[rowIndex - 1][columnIndex - 1]
        else:
            raise OutOfIndex()
        return entry


if __name__ == "__main__":
    tablero = Tablero(2,2)
    tablero.show()
    tablero.put_chip(2, 'rojo')
    tablero.show()
    print tablero.read_entry(2, 2)
