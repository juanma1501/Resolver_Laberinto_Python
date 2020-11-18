from Jsonfile import JsonFile
from State import State
import StatesSpace
class Problem:

    #Constructor
    def __init__(self, jsonfile):
        self.idInitial, self.IdObjective, self.json_path_to_maze = JsonFile.read_problem(jsonfile)




    def isObjective(self, state):
        return (state.getNeighbors() == [])

    def getInitialId(self):
        return self.initial

    def getObjectiveId(self):
        return self.objective

    def getMazePath(self):
        return self.json_path_to_maze

