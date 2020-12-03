from fileHandler import fileHandler
from State import State
import StatesSpace


class Problem:

    # Constructor
    def __init__(self, jsonfile, board=None):
        self.idInitial, self.IdObjective, self.json_path_to_maze = fileHandler.read_problem(jsonfile)
        if board is not None:
            try:
                self.rowI, self.colI = self.convert(self.idInitial)
                self.rowO, self.colO = self.convert(self.IdObjective)
            except AttributeError:
                print("ERROR. Tags of the json file must be INITIAL and OBJECTIVE.")
                exit()
            c = board[int(self.rowI), int(self.colI)]
            try:
                self.initialState = State((int(self.rowI), int(self.colI)), c.getLinks(), c.getValue())
            except AttributeError:
                print("ERROR. Change initial state.")
                exit()
        self.statesSpaces = StatesSpace.StatesSpace()

    # Getter of variable rowI
    def getRowI(self):
        return self.rowI

    # Getter of variable colI
    def getColI(self):
        return self.colI

    # Getter of variable rowO
    def getRowO(self):
        return self.rowO

    # Getter of variable colO
    def getColO(self):
        return self.colO

    # Getter of variable statesSpace
    def getStatesSpace(self):
        return self.statesSpaces

    #Function that returns True if the state that it is passed as argument
    # is the same as the objective one
    def isObjective(self, state):
        return state.getId() == self.IdObjective

    # Getter of variable initialId
    def getInitialId(self):
        return self.idInitial

    # Getter of variable initialState
    def getInitialState(self):
        return self.initialState

    # Getter of variable objectiveId
    def getObjectiveId(self):
        return self.IdObjective

    def getMazePath(self):
        return self.json_path_to_maze

    '''This method is used to get the values of the initial and objective state
    from the JSON file'''
    def convert(self, id_string):
        start = id_string.index('(')
        end = id_string.index(',')
        row = id_string[start + 1: end]

        start = id_string.index(' ')
        end = id_string.index(')')
        col = id_string[start + 1: end]
        return row, col
