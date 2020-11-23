###############################################################################
#   Name of the class: maze
#   Date of creation: 19/10/2020
#   Description:   The main class of the project, used to join all classes and
#                  manage the command line using argparse library.
################################################################################

import argparse

import Search
from Board import Board
from Draw import Draw
from Jsonfile import JsonFile
from Wilson import Wilson
from Problem import Problem

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

    json_param = subparser.add_parser('problem', help="Write the path of the Json file of the problem and the strategy")
    json_param = json_param.add_argument_group()
    json_param.add_argument('path', type=str, help='Write the path of the Json file of the problem.')
    json_param.add_argument('strategy', type=str, help='Write the strategy to solve the maze.')

    args = parser.parse_args()

    if args.subparser_name == "console":
        g = Board(args.r, args.c)
        Wilson.create(g)
        print(g)
    elif args.subparser_name == "image":
        g = Board(args.r, args.c)
        Wilson.create(g)
        Draw(g, 'Maze ' + str(g.rows) + 'x' + str(g.columns)).draw(fromjson=False)
    elif args.subparser_name == "json":
        g = JsonFile.create_from_json(args.path)
        if JsonFile.check_consistency(args.path):  # We check the consistency of the json file
            Draw(g, 'Maze ' + str(g.rows) + 'x' + str(g.columns)).draw(fromjson=True)
        else:
            print("The introduced JSON file is not consistent."
                  "---END OF THE PROGRAM---")

    elif args.subparser_name == "problem":
        strategy = args.strategy

        if strategy == "BREADTH" or strategy == "DEPTH" or strategy == "UNIFORM" or strategy == "GREEDY" or strategy == "A":
            prob = Problem(args.path)
            g = JsonFile.create_from_json(prob.getMazePath())

            if JsonFile.check_consistency(prob.getMazePath()):  # We check the consistency of the json file
                prob = Problem(args.path, board=g)
                solution = Search.search(prob, 1000000, strategy)

                if solution is not None:
                    Search.Search.writeSolution(solution, g, prob)
                    JsonFile.create_txt_solution(solution, g, strategy)
                else:
                    print("NO SOLUTION WAS FOUND")

                Draw(g, 'Maze ' + str(g.rows) + 'x' + str(g.columns)).draw(fromjson=True)
            else:
                print("The introduced JSON file is not consistent."
                      "---END OF THE PROGRAM---")
        else:
            print("Introduce a valid strategy: "
                  "BREADTH, DEPTH, UNIFORM,  or A")
