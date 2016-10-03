#!/usr/bin/env python

import sys
import numpy


class ColumnIsFull(Exception):

    def __init___(self, column_index):
        self.failedcolumn_index = column_index


class OutOfIndex(Exception):

    def __init___(self, errArguments):
        self.arrayType = errArguments['type']
        self.index = errArguments['index']


class GameBoard(object):
    ROWSCOUNT = 6
    COLUMNSCOUNT = 7

    def __init__(self):
        self._matrix = self._generate_matrix(
            self.ROWSCOUNT, self.COLUMNSCOUNT, '-')
        self._winner = None

    def _generate_matrix(self, rows, columns, fill):
        """Return a numpy matrix of the desired dimensions

        Args:
            rows: the desired number of rows
            columns: the desired number of columns
            fill: the desired character or string to fill the matrix with
        Returns:
            a numpy array
        """
        char_array = numpy.full((rows, columns), fill, dtype='a5')
        return char_array

    def _retreive_column(self, column_index):
        return self._matrix[:, column_index - 1][::-1]


    def _array_contains(self, array_small, array_big):
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

    def _winner_in_array(self, testing_array):
        FOUR_RED_IN_A_ROW = numpy.full(4, 'red', dtype='a5')
        FOUR_BLUE_IN_A_ROW = numpy.full(4, 'blue', dtype='a5')
        if self._array_contains(FOUR_RED_IN_A_ROW, testing_array):
            self._winner = 'red'
            return True
        elif self._array_contains(FOUR_BLUE_IN_A_ROW, testing_array):
            self._winner = 'blue'
            return True
        else:
            return False

    def _check_rows_for_winner(self):
        """Check if there's a winner row-wise"""
        for i in range(self.ROWSCOUNT):
            if self._winner_in_array(self._matrix[i]):
                return True
        return False

    def _check_columns_for_winner(self):
        """Check if there's a winner column-wise"""
        for i in range(self.COLUMNSCOUNT):
            if self._winner_in_array(self._retreive_column(i)):
                return True
        return False

    def _check_diagonals_for_winner(self):
        """Check if there's a winner diagonal-wise"""
        for i in range(-2, 4):
            if self._winner_in_array(self._matrix.diagonal(i)) or self._winner_in_array(numpy.flipud(self._matrix).diagonal(i)):
                return True
        return False

    def _validate_matrix(self, matrix_to_test):
        """Checks if an input matrix have valid characters and structure

        Args:
            matrix_to_test: numpy array with dtype='a5'
        Returns
            a boolean value
        """
        valid_entries = ('-', 'blue', 'red')
        if matrix_to_test.shape != (6,7):
            return False
        for row in matrix_to_test:
            for entry in row:
                if entry in valid_entries:
                    pass
                else:
                    return False
        # TODO: Add structure validation (no "floating" entries in matrix)
        return True

    def show(self):
        """Print the game board in a nice format"""
        for row in self._matrix:
            for entry in row:
                print '{:4}'.format(entry),
            print
        print

    def set_board_from_matrix(self, external_matrix):
        """Set the internal game matrix with an external one, only if valid

        Args:
            external_matrix: numpy array with dtype='a5'
        Returns
            a boolean value
        """
        if self._validate_matrix(external_matrix):
            self._matrix = external_matrix
            return True
        return False

    def put_chip(self, column_index, color):
        """Inserts a new chip into the game matrix

        Args:
            column_index: the column where the chip is being put
            color: the color of the chip
        """
        try:
            rowIndex = self.ROWSCOUNT - \
                list(self._retreive_column(column_index)).index('-') - 1
            self._matrix[rowIndex][column_index - 1] = color.lower()
        except ValueError:
            raise ColumnIsFull(column_index)

    def read_entry(self, rowIndex, column_index):
        """Read a determined entry from the game matrix

        Args:
            rows: the desired number of rows
            columns: the desired number of columns
            fill: the desired character or string to fill the matrix with
        Returns
            the value encountered on the entry
        """
        if rowIndex <= self.ROWSCOUNT:
            if column_index <= self.COLUMNSCOUNT:
                entry = self._matrix[self.ROWSCOUNT - rowIndex][column_index - 1]
            else:
                raise OutOfIndex({'type': 'column', 'number': column_index})
        else:
            raise OutOfIndex({'type': 'row', 'index': rowIndex})
        return entry

    def winner_exists(self):
        """Check if there's a winner of the game and prints a message"""
        self._check_rows_for_winner()
        self._check_columns_for_winner()
        self._check_diagonals_for_winner()
        if self._winner:
            return True
        else:
            return False
