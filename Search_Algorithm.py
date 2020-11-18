import Stack
import Node
import Frontier
import StatesSpace
import State

solutionFile = "solution.txt"

strategys = ["BREADTH", "DEPTH", "UNIFORM", "GREEDY", "A*"]
generatedNodes = 0


def writeSolution(solution, final_node, strategy, problem):
    with open(solutionFile, 'w') as f:
        print("[id][cost,state,father_id,action,depth,h,value]")
        for node in solution:
            print("[" + node.getId() + "][" + node.getCost() + "," + node.getState() + "," + node.getParentId() + ","
                  + node.getAction() + "," + node.getDepth() + ","
                  + node.getHeuristic() + "," + node.getF() + "]")


def create_node(parent, state, cost, strategy, action):
    node = Node.Node(parent, state, cost, strategy, action)
    return node


def createListNodesTree(ls, parent, max_depth, strategy):
    ln = []
    if parent.getDepth() < max_depth:
        for successor in ls:
            action = successor[0]
            state = successor[1]
            cost = successor[2]
            node = create_node(parent, state, cost, strategy, action)
            ln.append(node)

    return ln


def createSolution(node):
    stack = Stack.Stack()
    nodeTree = node

    while not (nodeTree.getParent == None):
        stack.push(nodeTree)
        nodeTree = nodeTree.getParent
    stack.push(nodeTree)

    solution = []
    while not stack.isEmpty():
        solution.append(stack.pop())

    return solution


def cut(dictCut, ln, strategy):
    listNodesCut = []

    for node in ln:
        stateNode = node.getState()
        idState = stateNode.getId
        f_state = node.getF()

        if (idState in dictCut):
            if strategy == "DEPTH":
                if f_state > int(dictCut.get(idState)):
                    dictCut.update({idState: f_state})
                    listNodesCut.append(node)
            else:
                if f_state < int(dictCut.get(idState)):
                    dictCut.update({idState: f_state})
                    listNodesCut.append(node)
        else:
            dictCut.update({idState: f_state})
            listNodesCut.append(node)
    return listNodesCut, dictCut


def search(prob, strategy, depth):
    dictCut = {}
    frontier = Frontier.Frontier
    initial_state = prob.getInitial()
    initial_node = create_node(None, initial_state, 0, strategy, None)
    frontier.insert(initial_node)
    solution = None

    while ((solution == None) and (not (frontier.isEmpty()))):
        current_node = frontier.delete()
        current_state = current_node.getState()
        if prob.isObjective(current_state):
            solution = True
        else:
            ls = StatesSpace.StatesSpace.successors(current_state)
            ln = createListNodesTree(ls, current_node, depth, strategy)
            listCutNodes, dictCut = cut(dictCut, ln, strategy)
            frontier.insert(listCutNodes)

        if (solution == None):
            return None, None
        else:
            return createSolution(current_node), current_node


def search_solution(prob, strategy, max_depth):
    current_depth = 0
    solution = None

    while (solution == None) and (current_depth <= max_depth):
        solution, final_node = search(prob, strategy, current_depth)
        current_depth = current_depth + 1

    return solution, final_node
