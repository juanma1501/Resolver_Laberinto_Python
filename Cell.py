import random


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
        self.value = random.randint(0, 3)
        self.solution = None
        self.links = dict()  # Dictionary to store links, each key of the dictionary is a cell.

    #Getter of variable row
    def getRow(self):
        return self.row

    # Getter of variable column
    def getColumn(self):
        return self.column

    # Getter of variable value
    def getValue(self):
        return self.value

    """Print a cell (r, c)"""

    def __str__(self):
        return "(" + str(self.row) + ", " + str(self.column) + ")" + "value: " + str(self.value)

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

    def getNeighbours(self):
        neighbours = []
        if self.cellNorth:
            neighbours.append(self.cellNorth)
        if self.cellEast:
            neighbours.append(self.cellEast)
        if self.cellSouth:
            neighbours.append(self.cellSouth)
        if self.cellWest:
            neighbours.append(self.cellWest)
        return neighbours

    # Getter of variable links
    def getLinks(self):
        links = []
        if self.isLinked(self.cellNorth):
            links.append(self.cellNorth)

        if self.isLinked(self.cellEast):
            links.append(self.cellEast)

        if self.isLinked(self.cellSouth):
            links.append(self.cellSouth)

        if self.isLinked(self.cellWest):
            links.append(self.cellWest)

        return links
