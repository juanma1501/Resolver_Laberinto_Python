from Node import Node
from Frontier import Frontier
from StatesSpace import StatesSpace


class Search:

    def __init__(self):
        pass

    def writeSolution(solution, board, prob):
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
                row, col = prob.convert(node.getState().getId())
                board[int(row), int(col)].solution = True
            else:
                print("[" + str(node.getId()) + "][" + str(node.cost) + "," + str(node.getState().getId()) + "," + str(
                    node.getParent().getId()) + "," + str(node.getAction()) + "," + str(node.getDepth()) + "," + str(
                    node.getHeuristic()) + "," + str(node.getF()) + "]")
                row, col = prob.convert(node.getState().getId())
                board[int(row), int(col)].solution = True

            i += 1
        solution.reverse()


def expand_node(problem, node, strategy):
    node_list = []

    for successor in problem.statesSpaces.successors(node.state, problem):
        node_son = Node(node, successor[1], node.getCost() + successor[2], strategy, successor[0], node.depth + 1)
        node_son.heuristic = StatesSpace.heuristic_calculation(node_son.state, int(problem.getRowO()),
                                                               int(problem.getColO()))
        node_son.f = node_son.strategy(strategy)
        node_list.append(node_son)
    return node_list


def search(problem, depth, strategy):
    visitados = []
    fringe = Frontier()
    node = Node(None, problem.getInitialState(), 0, strategy, None, 0)
    rowI = problem.getRowI()
    colI = problem.getColI()
    rowO = problem.getRowO()
    colO = problem.getColO()
    node.heuristic_calculation(int(rowI), int(colI),
                               int(rowO), int(colO))
    node.f = node.strategy(strategy)

    fringe.insert(node)
    solution = False

    while (fringe.isEmpty() is not True) and (solution is False):
        node = fringe.delete()
        if problem.getObjectiveId() == node.state.getId():
            solution = True
        else:
            if not (node.getState().getId() in visitados) and (node.depth < depth):
                visitados.append(node.getState().getId())
                son_node_list = expand_node(problem, node, strategy)
                for son_node in son_node_list:
                    fringe.insert(son_node)

    if solution:
        return way(node)
    else:
        return None


def way(node):
    sol = []
    while node.getParent() is not None:
        sol.append(node)
        node = node.getParent()
    sol.append(node)
    return sol
