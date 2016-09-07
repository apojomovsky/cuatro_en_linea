#!/usr/bin/env python
import sys

class ColumnIsFull(Exception):
    pass

class Tablero(object):
    def __init__(self, intRows, intColumns):
        if intRows > 0 and intColumns > 0:
            self.rows = intRows
            self.columns = intColumns
            self.gameboard = [[None]*self.columns for _ in range(self.rows)]
        else:
            print "Invalid game board size"
            sys.exit(1)

    def show(self):
        for row in self.gameboard:
            for entry in row:
                print '{:4}'.format(entry),
            print
        print

    def put_chip(self, columnIndex, color):
        try:
            rowIndex = self.rows - list(reversed([row[columnIndex - 1] for row in self.gameboard])).index(None) - 1
            self.gameboard[rowIndex][columnIndex - 1] = color
        except ValueError:
            raise ColumnIsFull()

    def read_entry(self, rowIndex, columnIndex):
        try:
            entry = self.gameboard[rowIndex - 1][columnIndex - 1]
        except IndexError:
            print "Can't access an item from an invalid position."
            return None
        return entry


if __name__ == "__main__":
    tablero = Tablero(2,2)
    tablero.show()
    tablero.put_chip(2, 'rojo')
    tablero.show()
    print tablero.read_entry(2, 2)
