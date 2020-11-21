###############################################################################
#   Name of the class: maze
#   Date of creation: 19/10/2020
#   Description:   The main class of the project, used to join all classes and
#                  manage the command line using argparse library.
################################################################################

import argparse

import Busqueda_gualo
from Board import Board
from Draw import Draw
from Jsonfile import JsonFile
from Wilson import Wilson
from Problem import Problem
import Search_Algorithm

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(title='Console or PNG', dest='subparser_name')

    console_param = subparser.add_parser('console', help="Draw a maze in the console.")
    console_param = console_param.add_argument_group()
    console_param.add_argument('r', type=int, help="Number of rows")
    console_param.add_argument('c', type=int, help="Number of columns")

    image_param = subparser.add_parser('image', help="Draw a maze in a graphical way.")
    img_rc_group = image_param.add_argument_group()
    img_rc_group.add_argument('r', type=int, help="Number of rows")
    img_rc_group.add_argument('c', type=int, help="Number of columns")

    json_param = subparser.add_parser('json', help="Write the path of the Json file.")
    json_param = json_param.add_argument_group()
    json_param.add_argument('path', type=str, help='Write the path of the Json file.')

    json_param = subparser.add_parser('problem', help="Write the path of the Json file of the problem.")
    json_param = json_param.add_argument_group()
    json_param.add_argument('path', type=str, help='Write the path of the Json file of the problem.')

    args = parser.parse_args()
    if args.subparser_name == "console":
        g = Board(args.r, args.c)
        Wilson.create(g)
        print(g)
    elif args.subparser_name == "image":
        g = Board(args.r, args.c)
        Wilson.create(g)
        Draw(g, 'Maze ' + str(g.rows) + 'x' + str(g.columns)).draw()
    elif args.subparser_name == "json":
        g = JsonFile.create_from_json(args.path)
        if JsonFile.check_consistency(args.path):  # We check the consistency of the json file
            Draw(g, 'Maze ' + str(g.rows) + 'x' + str(g.columns)).draw()
        else:
            print("The introduced JSON file is not consistent."
                  "---END OF THE PROGRAM---")

    elif args.subparser_name == "problem":

        prob = Problem(args.path)
        g = JsonFile.create_from_json(prob.getMazePath())
        if JsonFile.check_consistency(prob.getMazePath()):  # We check the consistency of the json file

            prob = Problem(args.path, board=g)
            solution = Busqueda_gualo.search(prob, 1000000, 'GREEDY')
            if (solution is not None):
                Busqueda_gualo.writeSolution(solution, 'GREEDY', prob)
                print("Algoritmo completado con éxito")
            else:
                print("No se ha encontrado solucion")

            Draw(g, 'Maze ' + str(g.rows) + 'x' + str(g.columns)).draw()
        else:
            print("The introduced JSON file is not consistent."
                  "---END OF THE PROGRAM---")







