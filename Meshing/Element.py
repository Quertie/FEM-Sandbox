from Meshing.Node import Node

class Element:
    def __init__(self, nodes : Node):
        self.Nodes = nodes
    
    def Contains(self, position : float):
        nodePositions = (self.Nodes[0].Position, self.Nodes[1].Position)
        lowerBound, upperBound = min(nodePositions), max(nodePositions)
        return lowerBound <= position <= upperBound