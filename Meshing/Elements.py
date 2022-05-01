from Meshing.Node import Node
from numpy import array

class Element:
    @property
    def Nodes(self):
        return self._nodes

    @property
    def MassMatrix(self):
        return None

    @property
    def IntervalSize(self):
        return self.Nodes[1].Position - self.Nodes[0].Position

    def __init__(self, nodes : Node):
        self._nodes = nodes
    
    def Contains(self, position : float):
        nodePositions = (self.Nodes[0].Position, self.Nodes[1].Position)
        lowerBound, upperBound = min(nodePositions), max(nodePositions)
        return lowerBound <= position <= upperBound

class LinearElement(Element):
    @property
    def MassMatrix(self):
        return 1/6 * array([[2, 1], [1, 2]]) * self.IntervalSize
