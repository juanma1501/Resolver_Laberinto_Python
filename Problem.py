from Jsonfile import JsonFile
from State import State
import StatesSpace


class Problem:

    # Constructor
    def __init__(self, jsonfile, board=None):
        self.idInitial, self.IdObjective, self.json_path_to_maze = JsonFile.read_problem(jsonfile)
        if board is not None:
            self.rowI, self.colI = self.convert(self.idInitial)
            self.rowO, self.colO = self.convert(self.IdObjective)
            c = board[int(self.rowI), int(self.colI)]
            self.initialState = State((int(self.rowI), int(self.colI)), c.getLinks(), 0, value=0)
        self.statesSpaces = StatesSpace.StatesSpace(board)

    def getRowI(self):
        return self.rowI

    def getColI(self):
        return self.colI

    def getRowO(self):
        return self.rowO

    def getColO(self):
        return self.colO

    def getStatesSpace(self):
        return self.statesSpaces

    def isObjective(self, state):
        return state.getId() == self.IdObjective

    def getInitialId(self):
        return self.idInitial

    def getInitialState(self):
        return self.initialState

    def getObjectiveId(self):
        return self.IdObjective

    def getMazePath(self):
        return self.json_path_to_maze

    def convert(self, id_string):
        start = id_string.index('(')
        end = id_string.index(',')
        row = id_string[start + 1: end]

        start = id_string.index(' ')
        end = id_string.index(')')
        col = id_string[start + 1: end]
        return row, col
