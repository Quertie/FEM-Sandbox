class Node:
    def __init__(self, position, nodeId):
        self.Position = position
        self.Id = nodeId

class Element:
    def __init__(self, nodes):
        self.Nodes = nodes

class Mesh:
    def __init__(self, elements):
        self.Elements = elements
