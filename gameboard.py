#!/usr/bin/env python

import sys
import numpy as np


class ColumnIsFull(Exception):

    def __init___(self, columnIndex):
        self.failedColumnIndex = columnIndex


class OutOfIndex(Exception):

    def __init___(self, errArguments):
        self.arrayType = errArguments['type']
        self.index = errArguments['index']


class GameBoard(object):
    ROWSCOUNT = 6
    COLUMNSCOUNT = 7
    TEST_ARRAY_RED = np.full(4, 'red', dtype='a5')
    TEST_ARRAY_BLUE = np.full(4, 'blue', dtype='a5')

    def __init__(self):
        self.matrix = self.generate_matrix(
            self.ROWSCOUNT, self.COLUMNSCOUNT, '-')
        self.winner = None

    def generate_matrix(self, rows, columns, fill):
        """Return a numpy matrix of the desired dimensions

        Args:
            rows: the desired number of rows
            columns: the desired number of columns
            fill: the desired character or string to fill the matrix with
        Returns:
            a numpy array
        """
        charar = np.full((rows, columns), fill, dtype='a5')
        return charar

    def show(self):
        """Print the game board in a nice format"""
        for row in self.matrix:
            for entry in row:
                print '{:4}'.format(entry),
            print
        print

    def retreive_column(self, columnIndex):
        return self.matrix[:, columnIndex - 1][::-1]

    def put_chip(self, columnIndex, color):
        """Inserts a new chip into the game matrix

        Args:
            columnIndex: the column where the chip is being put
            color: the color of the chip
        """
        try:
            rowIndex = self.ROWSCOUNT - \
                list(self.retreive_column(columnIndex)).index('-') - 1
            self.matrix[rowIndex][columnIndex - 1] = color.lower()
        except ValueError:
            raise ColumnIsFull(columnIndex)

    def read_entry(self, rowIndex, columnIndex):
        """Read a determined entry from the game matrix

        Args:
            rows: the desired number of rows
            columns: the desired number of columns
            fill: the desired character or string to fill the matrix with
        Returns:
            the value encountered on the entry
        """
        if rowIndex <= self.ROWSCOUNT:
            if columnIndex <= self.COLUMNSCOUNT:
                entry = self.matrix[self.ROWSCOUNT - rowIndex][columnIndex - 1]
            else:
                raise OutOfIndex({'type': 'column', 'number': columnIndex})
        else:
            raise OutOfIndex({'type': 'row', 'index': rowIndex})
        return entry

    def array_in_array(self, array_small, array_big):
        """Check if an array is part of another array

        Args:
            array_small: the array to be checked as part of array_big
            array_big: the array where array_small will be searched
        Returns:
            a boolean value with the result of the search
        """
        for i in range(len(array_big) - len(array_small) + 1):
            if array_small.tolist() == array_big[i:len(array_small) + i].tolist():
                return True
            else:
                continue
        return False

    def check_rows(self):
        """Check if there's a winner row-wise"""
        for i in range(self.ROWSCOUNT):
            if self.array_in_array(self.TEST_ARRAY_RED, self.matrix[i]):
                self.winner = 'red'
                return True
            if self.array_in_array(self.TEST_ARRAY_BLUE, self.matrix[i]):
                self.winner = 'blue'
                return True
        return False

    def check_columns(self):
        """Check if there's a winner column-wise"""
        for i in range(self.COLUMNSCOUNT):
            if self.array_in_array(
                    self.TEST_ARRAY_RED,
                    self.retreive_column(i)):
                self.winner = 'red'
                return True
            if self.array_in_array(
                    self.TEST_ARRAY_BLUE,
                    self.retreive_column(i)):
                self.winner = 'blue'
                return True
        return False

    def check_diagonals(self):
        """Check if there's a winner diagonal-wise"""
        for i in range(-2, 4):
            if self.array_in_array(
                self.TEST_ARRAY_RED,
                self.matrix.diagonal(i)) or self.array_in_array(
                self.TEST_ARRAY_RED,
                np.flipud(
                    self.matrix).diagonal(i)):
                self.winner = 'red'
                return True
            if self.array_in_array(
                self.TEST_ARRAY_BLUE,
                self.matrix.diagonal(i)) or self.array_in_array(
                self.TEST_ARRAY_BLUE,
                np.flipud(
                    self.matrix).diagonal(i)):
                self.winner = 'blue'
                return True
        return False

    def winner_exists(self):
        """Check if there's a winner of the game and prints a message"""
        self.check_rows()
        self.check_columns()
        self.check_diagonals()
        if self.winner:
            print "Color {0} is the new winner!".format(self.winner.capitalize())
            sys.exit(1)
        else:
            print "Nope"
