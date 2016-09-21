#!/usr/bin/env python

import sys
import numpy as np

class ColumnIsFull(Exception):
    pass

class OutOfIndex(Exception):
    pass

class GameBoard(object):
    ROWSCOUNT = 6
    COLUMNSCOUNT = 7
    def __init__(self):
        self.matrix = self.generate_matrix(self.ROWSCOUNT, self.COLUMNSCOUNT, '-')

    def generate_matrix(self, rows, columns, fill):
        charar = np.full((rows, columns), fill, dtype='a5')
        return charar

    def show(self):
        for row in self.matrix:
            for entry in row:
                print '{:4}'.format(entry),
            print
        print

    def retreive_column(self, columnIndex):
        return self.matrix[:,columnIndex - 1][::-1]

    def put_chip(self, columnIndex, color):
        try:
            rowIndex = self.ROWSCOUNT - list(self.retreive_column(columnIndex)).index('-') - 1
            self.matrix[rowIndex][columnIndex - 1] = color
        except ValueError:
            raise ColumnIsFull()

    def read_entry(self, rowIndex, columnIndex):
        if rowIndex <= self.ROWSCOUNT and columnIndex <= self.COLUMNSCOUNT:
            entry = self.matrix[self.ROWSCOUNT - rowIndex][columnIndex - 1]
        else:
            raise OutOfIndex()
        return entry
