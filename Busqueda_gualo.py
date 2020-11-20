from Node import Node
from State import State
from Frontier import Frontier
from StatesSpace import StatesSpace
solutionFile = "solution.txt"

strategys = ["BREADTH", "DEPTH", "UNIFORM", "GREEDY", "A*"]
generatedNodes = 0

def writeSolution(solution, strategy, problem):
    i = 0
    # with open(solutionFile, 'w') as f:
    print("[id][cost,state,father_id,action,depth,h,value]")
    for node in solution:
        print("["+str(node.getId())+"]["+str(node.cost)+","+str(node.getParent().getId())+","+str(node.getAction())+","+str(node.getDepth())+","+str(node.getHeuristic())+","+str(node.getF())+"]")

def expand_node(problem, node, strategy):
    node_list = []

    for successor in problem.statesSpaces.successors(node.state):
        node_son = Node(node, successor[1], node.getCost() + successor[2], strategy, successor[0], node.depth + 1)
        """node_son.state = successor[1]
        node_son.parentNode = node
        node_son.action = successor[0]
        node_son.depth = node.depth + 1
        node_son.cost = node.getCost() + successor[2]"""

        node_son.heuristic = StatesSpace.heuristic_calculation(node.state, int(problem.getObjectiveId()[1]), int(problem.getObjectiveId()[4]))
        node_son.f = node_son.strategy(strategy)
        node_list.append(node_son)
    return node_list

def search(problem, depth, strategy):
    visitados = []
    fringe = Frontier()
    node = Node(None, problem.getInitialState(), 0, strategy, None, 0)
    """node.parentNode = None
    node.state = problem.getInitialState()
    node.cost = 0
    node.depth = 0
    node.action = None
    node.f = node.strategy(strategy)"""
    fringe.insert(node)

    solution = False

    while (fringe.isEmpty() != True) and (solution == False):
        node = fringe.delete()

        if problem.getObjectiveId() == node.state.getId():
            solution = True
        elif not(node.state in visitados) and (node.depth < depth):
            visitados.append(node.state)
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
    return way
