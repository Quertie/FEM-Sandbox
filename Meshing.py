class Node:
    def __init__(self, position, nodeId):
        self.Position = position
        self.Id = nodeId

class Element:
    def __init__(self, nodes):
        self.Nodes = nodes
    
    def Contains(self, position):
        nodePositions = (self.Nodes[0].Position, self.Nodes[1].Position)
        lowerBound, upperBound = min(nodePositions), max(nodePositions)
        return lowerBound <= position <= upperBound

class Mesh:
    def __init__(self, elements):
        self.Elements = elements

    def CreateElements(nodes):
        return Mesh([Element([nodes[i], nodes[i+1]]) for i in range(len(nodes)-1)])

    def GetElementForPosition(self, x):
        for element in self.Elements:
            if element.Contains(x): return element