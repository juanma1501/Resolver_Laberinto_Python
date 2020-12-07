class Frontier:

    def __init__(self):
        self.listFrontier = []

    '''Method to insert a node passed as argument to the frontier 
    and sort it according to the criterion said by the teacher'''
    def insert(self, nodeTree):
        self.listFrontier.append(nodeTree)
        self.listFrontier = sorted(self.listFrontier)

    def insertList(self, ln):
        for node in ln:
            self.insert(node)

    '''Method to delete and get the first node of the frontier'''
    def delete(self):
        return self.listFrontier.pop(0)

    '''Method to check if the frontier is empty'''
    def isEmpty(self):
        return self.listFrontier == []
