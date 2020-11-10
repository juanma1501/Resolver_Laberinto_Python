from Jsonfile import JsonFile
from State import State

class Problem:

    #Constructor
    def __init__(self, jsonfile):
        self.initial, self.objective, self.json_path_to_maze = JsonFile.read_problem(jsonfile)

    def isObjective(self, state):
        return (State.getNeighbors() == [])

