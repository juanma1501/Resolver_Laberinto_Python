###############################################################################
#   Name of the class: Cell
#   Date of creation: 19/10/2020
#   Description:   Class to represent a cell, and it´s features such us it`s
#                  neighbors and links.
################################################################################

class Cell:

    """Constructor"""
    def __init__(self, row, column):
        self.column = column
        self.row = row
        self.cellNorth = None
        self.cellWest = None
        self.cellSouth = None
        self.cellEast = None
        self.links = dict()  # Dictionary to store links, each key of the dictionary is a cell.
        self.neighbors = self.getNeighbors()

    """Print a cell (r, c)"""
    def __str__(self):
        return "(" + str(self.row) + ", " + str(self.column) + ")"

    ###############################################################################################
    #     Name of the method: link
    #
    #     Date of creation: 19/10/2020
    #
    #     Description: Method to link a cell with another one
    #
    #     Parameters
    #          self
    #          cell -> the cell that we want to link with the one that call the method
    #          bol -> this method is recursive, so we need to stop it at any given time, so, when this parameter
    #                 is False, the method ends.
    #
    #     Return
    #          self
    ################################################################################################
    def link(self, cell, bol=True):
        self.links[cell] = True
        if bol:
            cell.link(self, False)
        return self

    """Method to know if a cell is linked with another one using links dictionary"""
    def isLinked(self, cell):
        return cell in self.links

    """Method to store in a list all the neighbors of a cell"""
    def getNeighbors(self):
        neighbors = []
        if self.cellNorth:
            neighbors.append(self.cellNorth)
        if self.cellSouth:
            neighbors.append(self.cellSouth)
        if self.cellWest:
            neighbors.append(self.cellWest)
        if self.cellEast:
            neighbors.append(self.cellEast)
        return neighbors
