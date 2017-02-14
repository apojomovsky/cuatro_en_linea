#!/usr/bin/env python
import numpy
from itertools import groupby
from copy import copy

class ColumnIsFull(Exception):
    def __init___(self, column_index):
        self.failedcolumn_index = column_index

class BoardIsFull(Exception):
    def __init___(self, matrix):
        self.matrix = matrix

class OutOfIndex(Exception):
    def __init___(self, errArguments):
        self.array_type = errArguments['type']
        self.index = errArguments['index']


class GameBoard(object):
    ROWSCOUNT = 6
    COLUMNSCOUNT = 7

    def __init__(self):
        self._matrix = self.generate_matrix(
            self.ROWSCOUNT, self.COLUMNSCOUNT, None)
        self._winner = None
        self._moves = []

    def __eq__(self, other_board):
        """ Checks if the _matrix from both gameboards have the same shape and elements"""
        if isinstance(other_board, self.__class__):
            other_board_iter = other_board._get_entries()
            for entry in self._get_entries():
                if not entry == other_board_iter.next():
                    return False
            return True
        return False

    def __ne__(self, other_board):
        """ Checks if the _matrix from both gameboards are differents"""
        return not self.__eq__(other_board)

    def __str__(self):
        representation = ''
        for row in self.get_rows():
            for entry in row:
                if entry is None:
                    representation = representation + '. '
                elif entry == 'red':
                    representation = representation + 'R '
                elif entry == 'blue':
                    representation = representation + 'B '
            representation = representation + "\n"
        return representation

    def columns_count(self):
        return self.COLUMNSCOUNT

    def is_column_full(self, column_number):
        return self._matrix[0, column_number - 1] is not None

    def playable_positions(self):
        positions = []
        for position in range(1, self.COLUMNSCOUNT + 1):
            if not self.is_column_full(position):
                positions.append(position)
        return positions

    def undo_move(self):
        move = self._moves.pop(-1)
        self._matrix[move[0]][move[1]] = None

    def copy(self):
        # Avoid calling __init__ and hence creating an unneeded matrix
        clone = GameBoard.__new__(GameBoard)
        clone._matrix = self._matrix.copy()
        clone._moves = list(self._moves)
        clone._winner = self._winner
        return clone

    def put_chip(self, column_index, color):
        """Inserts a new chip into the game matrix

        Args:
            column_index: the column where the chip is being put
            color: the color of the chip
        """
        self._raise_if_board_is_full()
        if not self.column_is_full(column_index):
            for row in range(self.ROWSCOUNT - 1, -1, -1):
                if self._matrix[row][column_index - 1] is None:
                    self._matrix[row][column_index - 1] = color
                    self._moves.append((row, column_index - 1, color))
                    return row
        else:
            raise ColumnIsFull(column_index)

    def retrieve_first_non_full_column(self):
        """Returns the index of the first non-full column
           found, looking from left to right on the board
        """
        self._raise_if_board_is_full()
        index_list = range(1, self.COLUMNSCOUNT + 1)
        for index in index_list:
            if not self.column_is_full(index):
                return index

    def retrieve_emptiest_column(self):
        """Returns the index of the emptiest column found on the board
        """
        self._raise_if_board_is_full()
        rows_index_list = range(1, self.ROWSCOUNT + 1)
        columns_index_list = range(1, self.COLUMNSCOUNT + 1)
        for row_index in rows_index_list:
            for column_index in columns_index_list:
                if self.read_entry(row_index, column_index) is None:
                    return column_index

    def count_same_color_on_top(self, column_index, color):
        """Reads the number of chips of the given color
           that are placed on top of the given column
        Args:
            column_index: the number of columnt to test
            color: the color to test
        Returns
            an integer with the count of same color chips on top
        """
        column = self._retrieve_column(column_index)
        if numpy.any(column):
            consecutive_groups = self._retrieve_consecutive_elements_from_array(column)
            for index, entry in enumerate(consecutive_groups):
                if None in entry:
                    consecutive_groups.pop(index)
            if consecutive_groups[-1][1] == color:
                return consecutive_groups[-1][0]
        return 0

    def count_free_entries_on_column(self, column_index):
        """Checks the number of 'None' entries on top of a given column"""
        column = self._retrieve_column(column_index)
        consecutive_groups = self._retrieve_consecutive_elements_from_array(column)
        if not self.column_is_full(column_index):
            return consecutive_groups[-1][0]
        return 0

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
        return self.winner_color() is not None

    def winner_color(self):
        """
        Check if there is a winner of any color. Note that this is very
        inefficient as we need to scan the complete board twice, one for each
        color. When possible, use winner_color_in_last_move, which is has way
        better performance.
        """
        if self._wins_in_any_row('red'):
            return 'red'
        if self._wins_in_any_row('blue'):
            return 'blue'

        if self._wins_in_any_column('red'):
            return 'red'
        if self._wins_in_any_column('blue'):
            return 'blue'

        if self._wins_in_any_diagonal('red'):
            return 'red'
        if self._wins_in_any_diagonal('blue'):
            return 'blue'

        return None

    def winner_color_in_last_move(self):
        """
        Answers if the last move generated a winner. We currently only use
        knowledge of the last move to search for a winner of that color.
        TODO: Restrict the search to only use the row/column/diagonals that
        involve the last played matrix cell.
        """
        (last_row, last_column, last_color) = self._moves[-1]
        if self._wins_in_row(last_color, last_row) or \
           self._wins_in_column(last_color, last_column) or \
           self._wins_in_any_diagonal(last_color):
            return last_color
        return None

    def _wins_in_any_row(self, color):
        for row in range(self.ROWSCOUNT - 1, -1, -1):
            if self._wins_in_row(color, row):
                return True
        return False

    def _wins_in_row(self, color, row):
        for column in range(0, self.COLUMNSCOUNT - 3):
            if self._matrix[row][column] == color and \
               self._matrix[row][column + 1] == color and \
               self._matrix[row][column + 2] == color and \
               self._matrix[row][column + 3] == color:
                return True
        return False

    def _wins_in_any_column(self, color):
        for column in range(0, self.COLUMNSCOUNT):
            if self._wins_in_column(color, column):
                return True
        return False

    def _wins_in_column(self, color, column):
        for row in range(0, self.ROWSCOUNT - 3):
            if self._matrix[row][column] == color and \
               self._matrix[row + 1][column] == color and \
               self._matrix[row + 2][column] == color and \
               self._matrix[row + 3][column] == color:
                return True
        return False

    def _wins_in_any_diagonal(self, color):
        """
        This definitely requires some love and be defined in terms of
        COLUMNSCOUNT and ROWSCOUNT.
        """
        return self._connects_four_in(color, (2, 0), (3, 1), (4, 2), (5, 3)) or \
               self._connects_four_in(color, (2, 1), (3, 2), (4, 3), (5, 4)) or \
               self._connects_four_in(color, (2, 2), (3, 3), (4, 4), (5, 5)) or \
               self._connects_four_in(color, (2, 3), (3, 4), (4, 5), (5, 6)) or \
               self._connects_four_in(color, (1, 0), (2, 1), (3, 2), (4, 3)) or \
               self._connects_four_in(color, (1, 1), (2, 2), (3, 3), (4, 4)) or \
               self._connects_four_in(color, (1, 2), (2, 3), (3, 4), (4, 5)) or \
               self._connects_four_in(color, (1, 3), (2, 4), (3, 5), (4, 6)) or \
               self._connects_four_in(color, (0, 0), (1, 1), (2, 2), (3, 3)) or \
               self._connects_four_in(color, (0, 1), (1, 2), (2, 3), (3, 4)) or \
               self._connects_four_in(color, (0, 2), (1, 3), (2, 4), (3, 5)) or \
               self._connects_four_in(color, (0, 3), (1, 4), (2, 5), (3, 6)) or \
               self._connects_four_in(color, (2, 6), (3, 5), (4, 4), (5, 3)) or \
               self._connects_four_in(color, (2, 5), (3, 4), (4, 3), (5, 2)) or \
               self._connects_four_in(color, (2, 4), (3, 3), (4, 2), (5, 1)) or \
               self._connects_four_in(color, (2, 3), (3, 2), (4, 1), (5, 0)) or \
               self._connects_four_in(color, (1, 6), (2, 5), (3, 4), (4, 3)) or \
               self._connects_four_in(color, (1, 5), (2, 4), (3, 3), (4, 2)) or \
               self._connects_four_in(color, (1, 4), (2, 3), (3, 2), (4, 1)) or \
               self._connects_four_in(color, (1, 3), (2, 2), (3, 1), (4, 0)) or \
               self._connects_four_in(color, (0, 6), (1, 5), (2, 4), (3, 3)) or \
               self._connects_four_in(color, (0, 5), (1, 4), (2, 3), (3, 2)) or \
               self._connects_four_in(color, (0, 4), (1, 3), (2, 2), (3, 1)) or \
               self._connects_four_in(color, (0, 3), (1, 2), (2, 1), (3, 0))


    def _connects_four_in(self, color, position_1, position_2, position_3, position_4):
        """
        Only used in _wins_in_any_diagonal, maybe will go away in the future.
        """
        return self._matrix[position_1[0]][position_1[1]] == color and \
               self._matrix[position_2[0]][position_2[1]] == color and \
               self._matrix[position_3[0]][position_3[1]] == color and \
               self._matrix[position_4[0]][position_4[1]] == color

    def board_is_full(self):
        """Checks whether a board is full or not"""
        return len(self._moves) == 42

    def is_game_over(self):
        """Checks whether the game is over or not"""
        return self.winner_exists() or self.board_is_full()

    def get_rows(self):
        """Returns an iterator object that will get all the rows from the board"""
        for row in self._matrix:
            yield list(row.tolist())

    @classmethod
    def from_matrix(cls, external_matrix):
        """Returns an instance of GameBoard with a custom _matrix attribute"""
        board = GameBoard()
        if board.set_board_from_matrix(external_matrix):
            return board
        else:
            return None

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

    def generate_matrix(self, rows, columns, fill):
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
        return self._matrix[0][column_index - 1] is not None

    def row_is_full(self, row_index):
        """Checks if the row on a given index is full or not"""
        for entry in self._matrix[row_index +1]:
            if not entry:
                return False
        return True

    def _retrieve_consecutive_elements_from_array(self, array):
        """Reads the consecutive elements from a given array
        Args:
            array: a numpy array
        Returns
            a list of elements conformed by: (element, number_of_repetitions)
            element: object of the same kind as the one from the array
            number_of_repetitions: the number of consecutive repetitions
        """
        return [(sum(1 for occurrence in iterator), entry) for entry, iterator in groupby(array)]

    def _get_entries(self):
        """Returns an iterator object that will get all the entries from the board"""
        for row in self._matrix:
            for entry in row:
                yield copy(entry)

    def _get_columns(self):
        """Returns an iterator object that will get all the columns from the board"""
        for column_index in range(1, self.COLUMNSCOUNT + 1):
            yield list(self._retrieve_column(column_index))

    def _get_diagonals(self):
        """Returns an iterator object that will get all the diagonals with more
           than 3 elements from the board
        """
        for i in range(-2, 4):
            yield list(self._matrix.diagonal(i))
        for i in range(-2, 4):
            yield list(numpy.flipud(self._matrix).diagonal(i))

    def _raise_if_board_is_full(self):
        if self.board_is_full():
            raise BoardIsFull(self._matrix)

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


    def _validate_matrix(self, matrix_to_test):
        """Checks if an input matrix have valid characters and structure

        Args:
            matrix_to_test: list
        Returns
            a boolean value
        """
        matrix_to_test = numpy.asarray(matrix_to_test)
        if matrix_to_test.shape != (6,7):
            return False
        for row in matrix_to_test:
            if not all(self._is_valid_cell_value(entry) for entry in row):
                return False
        for column_index in range(self.COLUMNSCOUNT):
            column = matrix_to_test[:, column_index]
            indices = [index for index, entry in enumerate(column) if entry == None]
            if indices:
                if indices != [number for number in range(len(indices))]:
                    return False
        return True

    def _is_valid_cell_value(self, entry):
        """Checks if a given value is a valid entry"""
        valid_entries = (None, 'blue', 'red')
        return entry in valid_entries
