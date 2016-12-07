#!/usr/bin/env python
import numpy

class ColumnIsFull(Exception):

    def __init___(self, column_index):
        self.failedcolumn_index = column_index


class OutOfIndex(Exception):

    def __init___(self, errArguments):
        self.array_type = errArguments['type']
        self.index = errArguments['index']


class GameBoard(object):
    ROWSCOUNT = 6
    COLUMNSCOUNT = 7

    def __init__(self):
        self._matrix = self._generate_matrix(
            self.ROWSCOUNT, self.COLUMNSCOUNT, None)
        self._winner = None

    def put_chip(self, column_index, color):
        """Inserts a new chip into the game matrix

        Args:
            column_index: the column where the chip is being put
            color: the color of the chip
        """
        if not self.column_is_full(column_index):
            rowIndex = self.ROWSCOUNT - \
                list(self._retrieve_column(column_index)).index(None) - 1
            self._matrix[rowIndex][column_index - 1] = color.lower()
        else:
            raise ColumnIsFull(column_index)

    def retrieve_first_non_full_column(self):
        """Docstring goes here
        """
        index_list = range(1, self.COLUMNSCOUNT + 1)
        for index in index_list:
            if not self.column_is_full(index):
                return index

    def retrieve_emptiest_column(self):
        """Docstring goes here
        """
        rows_index_list = range(1, self.ROWSCOUNT + 1)
        columns_index_list = range(1, self.COLUMNSCOUNT + 1)
        for row_index in rows_index_list:
            for column_index in columns_index_list:
                if self.read_entry(row_index, column_index) is None:
                    return column_index

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

    def winner_color(self):
        """Returns the color of the winner if it exists"""
        if self.winner_exists():
            return self._winner
        return False

    def board_is_full(self):
        """Checks whether a board is full or not"""
        for row in self._matrix:
            for entry in row:
                if entry is None:
                    return False
        return True

    def game_over(self):
        """Checks whether the game is over or not"""
        if self.winner_exists() or self.board_is_full():
            return True
        return False

    @classmethod
    def from_matrix(cls, external_matrix):
        """Returns an instance of GameBoard with a custom _matrix attribute"""
        board = GameBoard()
        if board.set_board_from_matrix(external_matrix):
            return board
        else:
            return False

    def set_board_from_matrix(self, matrix):
        """Set the internal game matrix with an external one, only if valid

        Args:
            external_matrix: numpy array with dtype=object
        Returns
            a boolean value
        """
        numpy_matrix = numpy.asarray(matrix)
        if self._validate_matrix(numpy_matrix):
            self._matrix = numpy_matrix
            return True
        return False

    def _generate_matrix(self, rows, columns, fill):
        """Return a numpy matrix of the desired dimensions

        Args:
            rows: the desired number of rows
            columns: the desired number of columns
            fill: the desired character or string to fill the matrix with
        Returns:
            a numpy array
        """
        char_array = numpy.full((rows, columns), fill, dtype=object)
        return char_array

    def column_is_full(self, column_index):
        """Checks if the column on a given index is full or not"""
        return self._retrieve_column(column_index)[5] is not None

    def row_is_full(self, row_index):
        """Checks if the row on a given index is full or not"""
        for entry in self._matrix[row_index +1]:
            if not entry:
                return False
        return True

    def _retrieve_column(self, column_index):
        """Returns an inverted column for a given index"""
        return self._matrix[:, column_index - 1][::-1]

    def _array_contains(self, array_small, array_big):
        """Check if an array is part of another array

        Args:
            array_small: the array to be checked as part of array_big
            array_big: the array where array_small is attempted to be found
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
        """Check if there's a four-in-a-row occurrence on a given array"""
        FOUR_RED_IN_A_ROW = numpy.full(4, 'red', dtype=object)
        FOUR_BLUE_IN_A_ROW = numpy.full(4, 'blue', dtype=object)
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
            if self._winner_in_array(self._retrieve_column(i)):
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
            matrix_to_test: numpy array with dtype=object
        Returns
            a boolean value
        """
        valid_entries = (None, 'blue', 'red')
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
