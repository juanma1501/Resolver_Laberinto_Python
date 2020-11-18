from Jsonfile import JsonFile
from Cell import Cell
from State import State
import StatesSpace
class Problem:

    #Constructor
    def __init__(self, jsonfile, board= None):
        self.idInitial, self.IdObjective, self.json_path_to_maze = JsonFile.read_problem(jsonfile)
        print(self.getObjectiveId())
        if board is not None:
            c = board[int(self.idInitial[1]), int(self.idInitial[4])]
            self.initialState = State((self.idInitial[1], self.idInitial[4]), c.getLinks(), 0)
        self.statesSpaces = StatesSpace.StatesSpace(board)


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

