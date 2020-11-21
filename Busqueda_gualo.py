from Node import Node
from State import State
from Frontier import Frontier
from StatesSpace import StatesSpace
solutionFile = "solution.txt"

strategys = ["BREADTH", "DEPTH", "UNIFORM", "GREEDY", "A*"]
generatedNodes = 0

def writeSolution(solution, strategy, problem):
    i = 0
    solution.reverse()
    print("[id][cost,state,father_id,action,depth,h,value]")
    for node in solution:
        if i == 0:
            print("[" + str(node.getId()) + "][" + str(node.cost) + "," + str(
                node.getState().getId()) + "," + str(
                node.getParent()) + "," + str(node.getAction()) + "," + str(
                node.getDepth()) + "," + str(
                node.getHeuristic()) + "," + str(node.getF()) + "]")
        else:
            print("[" + str(node.getId()) + "][" + str(node.cost) + "," + str(node.getState().getId()) + "," + str(
                node.getParent().getId()) + "," + str(node.getAction()) + "," + str(node.getDepth()) + "," + str(
                node.getHeuristic()) + "," + str(node.getF()) + "]")
        i += 1

def expand_node(problem, node, strategy):
    node_list = []

    for successor in problem.statesSpaces.successors(node.state, problem):
        node_son = Node(node, successor[1], node.getCost() + successor[2], strategy, successor[0], node.depth + 1)
        node_son.heuristic = StatesSpace.heuristic_calculation(node_son.state, int(problem.getObjectiveId()[1]), int(problem.getObjectiveId()[4]))
        node_son.f = node_son.strategy(strategy)
        node_list.append(node_son)
    return node_list

def search(problem, depth, strategy):
    visitados = []
    fringe = Frontier()
    node = Node(None, problem.getInitialState(), 0, strategy, None, 0)
    node.heuristic_calculation(int(problem.getInitialId()[1]), int(problem.getInitialId()[4]), int(problem.getObjectiveId()[1]), int(problem.getObjectiveId()[4]))
    node.f = node.strategy(strategy)
    fringe.insert(node)
    solution = False

    while (fringe.isEmpty() != True) and (solution == False):
        node = fringe.delete()
        if problem.getObjectiveId() == node.state.getId():
            solution = True
        elif not(node.getState().getId() in visitados) and (node.depth < depth):
            visitados.append(node.getState().getId())
            son_node_list = expand_node(problem, node, strategy)
            for son_node in son_node_list:
                fringe.insert(son_node)

    if solution:
        return way(node)
    else:
        return None

def way(node):
    way = []
    while(node.getParent() != None):
        way.append(node)
        node = node.getParent()
    way.append(node)
    node = node.getParent()
    return way
