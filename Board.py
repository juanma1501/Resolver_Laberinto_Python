###############################################################################
#   Name of the class: Board
#   Date of creation: 19/10/2020
#   Description:   This class is used to represent a board of N rows and M columns, formed by cells (NxM), where
#                  the maze is going to be created following Wilson´s algorithm.
################################################################################

from Cell import Cell
import random


class Board:

    """Constructor"""
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.board = self.make_board()
        self.set_neighbors()

    """Returns a cell of the board"""
    def __getitem__(self, pos):
        row, col = pos
        if ((self.rows - 1) >= row >= 0) and ((self.columns - 1) >= col >= 0):
            return self.board[row][col]
        return None

    """
       Method to make the board according to the number of rows and columns
       Returns: grid
    """
    def make_board(self):
        board = [[Cell(row, col)
                 for col in range(self.columns)]
                for row in range(self.rows)]
        return board

    """Method to iterate in all rows, yield is used as return to use it later in all_cells"""
    def all_rows(self):
        for row in self.board:
            yield row

    """Method to iterate in all cells"""
    def all_cells(self):
        for row in self.all_rows():
            for cell in row:
                yield cell

    """Get a random cell from the board"""
    def random_cell(self):
        col = random.randint(0, self.columns - 1)
        row = random.randint(0, self.rows - 1)
        return self[row, col]

    ###############################################################################################
    #     Name of the method: get_max_neighbors
    #
    #     Date of creation: 19/10/2020
    #
    #     Description: This method is used to calculate the max number of neighbors that a cell has
    #                  in the grid.
    #
    #     Parameters
    #          self
    #
    #     Return
    #          max -> integer number, the max number of neighbors
    ################################################################################################
    def get_max_neighbors(self):
        aux = 0
        max = 0
        for cell in self.all_cells():
            if cell.isLinked(cell.cellNorth): aux = aux + 1
            if cell.isLinked(cell.cellSouth): aux = aux + 1
            if cell.isLinked(cell.cellSouth): aux = aux + 1
            if cell.isLinked(cell.cellSouth): aux = aux + 1
            if aux > max: max = aux
            aux = 0
        return max

    ###############################################################################################
    #     Name of the method: get_max_neighbors
    #
    #     Date of creation: 19/10/2020
    #
    #     Description: Method to set the neighbors (N, S, W, E) of each cell in the grid.
    #
    #     Parameters
    #          self
    ################################################################################################
    def set_neighbors(self):
        for cell in self.all_cells():
            row, col = cell.row, cell.column
            cell.cellNorth = self[row - 1, col]
            cell.cellSouth = self[row + 1, col]
            cell.cellWest = self[row, col - 1]
            cell.cellEast = self[row, col + 1]

    """Return a tuple: rows and columns"""
    def size(self):
        return self.rows, self.columns

    def contents_of(self, cell):
        """ This routine returns the 'contents' of a cell object """
        return " "

    """Overloaded function used to print the maze in the console"""
    def __str__(self):
        output = '+' + "---+" * self.columns + '\n'
        for row in self.all_rows():
            top = '|'
            bottom = '+'
            for cell in row:
                body = '{:3s}'.format(self.contents_of(cell))
                east_boundary = ' ' if cell.isLinked(cell.cellEast) else '|'
                top = top + body + east_boundary
                south_boundary = '   ' if cell.isLinked(cell.cellSouth) else '---'
                corner = '+'
                bottom = bottom + south_boundary + corner
            output = output + top + '\n'
            output = output + bottom + '\n'
        return output