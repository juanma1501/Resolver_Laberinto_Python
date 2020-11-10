###############################################################################
#   Name of the class: jsonfile
#   Date of creation: 19/10/2020
#   Description:   This class is used to store methods related to Json files such us
#                  read, export, create mazes from Json files and check the consistency
#                  of a Json file.
################################################################################


# !/usr/bin/env python
import json
from Board import Board


class JsonFile:

    # Constructor
    def __init__(self):
        pass

    ##################################################################################
    # Name of the method: read
    #
    # Date of creation: 19/10/2020
    #
    # Description: a method to read the data from the json file
    #
    # Parameters:
    #     jsonFile -> the path of the Json file that we want to read
    #
    # Return:
    #     data -> a dictionary with the data of the Json
    #
    # Exceptions controlled:
    #     FileNotFoundError -> if the file does not exist or if the path is not well writed
    #     UnicodeDecodeError -> if the file is not .json
    ###################################################################################
    @staticmethod
    def read(jsonFile):
        try:
            jsondata = open(jsonFile).read()
            data = json.loads(jsondata)
            return data
        except FileNotFoundError:
            print("ERROR. File '{0}' not found".format(jsonFile))
            exit()
        except UnicodeDecodeError:
            print("ERROR. Please, insert a .json file.")
            exit()

    ###############################################################################################
    #     Name of the method: create_from_json
    #
    #     Date of creation: 19/10/2020
    #
    #     Description: this method prepare the cells of the grid with the data collected from
    #                  the json file
    #
    #     Parameters
    #          jsonFile -> the path of the Json file that we want to read
    #
    #     Return
    #          g -> the grid created with the links provided in the json file
    ################################################################################################
    @staticmethod
    def create_from_json(jsonFile):
        data = JsonFile.read(jsonFile)

        # We collect information from the Json File
        rows = data.get('rows')
        cols = data.get('cols')
        links = []  # En esta lista van a estar todos los true y false de todas las celdas

        # Create the grid
        g = Board(rows, cols)

        # Loop to store in a list named "links" the links of each each cell
        for i in range(rows):
            for j in range(cols):
                links.append(data.get('cells').get('(' + str(i) + ', ' + str(j) + ')').get('neighbors'))

        # Loop for link each cell with others
        i = 0
        for cell in g.all_cells():
            if links[i][0]:
                cell.link(cell.cellNorth)
                pass
            if links[i][1]:
                cell.link(cell.cellEast)
                pass
            if links[i][2]:
                cell.link(cell.cellSouth)
                pass
            if links[i][3]:
                cell.link(cell.cellWest)
            i = i + 1

        return g

    ################################################################################################
    #         Name of the method: export
    #
    #         Date of creation: 19/10/2020
    #
    #         Description: this method exports the json file with all the information of the maze
    #
    #         Parameters
    #              grid -> the grid(maze) that we want to export
    ################################################################################################
    @staticmethod
    def export(grid):
        data = {
            'rows': grid.rows,
            'cols': grid.columns,
            'max_n': grid.get_max_neighbors(),
            'mov': [
                [
                    -1,
                    0
                ],
                [
                    0,
                    1
                ],
                [
                    1,
                    0
                ],
                [
                    0,
                    -1
                ]
            ],
            'id_movs': [
                "N",
                "E",
                "S",
                "O"
            ],
            'cells': {}
        }

        for cell in grid.all_cells():
            links = [cell.isLinked(cell.cellNorth), cell.isLinked(cell.cellEast), cell.isLinked(cell.cellSouth),
                     cell.isLinked(cell.cellWest)]
            data['cells']['({}, {})'.format(cell.row, cell.column)] = {'value': 0, 'neighbors': links}

        with open('Maze ' + str(grid.rows) + 'x' + str(grid.columns) + '.json', 'w') as file:
            json.dump(data, file, indent=4)

    ###############################################################################################
    #     Name of the method: check_consistency
    #
    #     Date of creation: 19/10/2020
    #
    #     Description: this method checks if there is any inconsistency in the json file
    #
    #     Parameters
    #          jsonFile -> the path of the Json file that we want to read
    #
    #     Return
    #          consistent -> boolean, True if the file is consistent and False if the file is not consistent
    ################################################################################################
    @staticmethod
    def check_consistency(jsonFile):
        data = JsonFile.read(jsonFile)
        consistent = True

        # We collect information from the Json File
        rows = data.get('rows')
        cols = data.get('cols')

        # Create the grid
        g = Board(rows, cols)

        # Loop for search inconsistencies
        for i in range(rows):
            for j in range(cols):

                cell = data.get('cells').get('(' + str(i) + ', ' + str(j) + ')').get('neighbors')

                if (j - 1) >= 0:
                    west_cell = data.get('cells').get('(' + str(i) + ', ' + str(j - 1) + ')').get('neighbors')
                    if west_cell[1] != cell[3]:
                        consistent = False
                        return consistent

                if (i - 1) >= 0:
                    north_cell = data.get('cells').get('(' + str(i - 1) + ', ' + str(j) + ')').get('neighbors')
                    if north_cell[2] != cell[0]:
                        consistent = False
                        return consistent

                if (j + 1) <= (g.columns - 1):
                    east_cell = data.get('cells').get('(' + str(i) + ', ' + str(j + 1) + ')').get('neighbors')
                    if east_cell[3] != cell[1]:
                        consistent = False
                        return consistent

                if (i + 1) <= (g.rows - 1):
                    south_cell = data.get('cells').get('(' + str(i + 1) + ', ' + str(j) + ')').get('neighbors')
                    if south_cell[0] != cell[2]:
                        consistent = False
                        return consistent
        return consistent

    @staticmethod
    def read_problem(jsonFile):
        data = JsonFile.read(jsonFile)

        # We collect information from the Json File
        initial = data.get('INITIAL')
        objective = data.get('OBJECTIVE')
        json_path_to_maze = data.get('MAZE')

        return initial, objective, json_path_to_maze
