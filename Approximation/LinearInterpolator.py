from typing import Iterable
from Meshing.Node import Node
from Approximation.Function import Function

class LinearInterpolator(Function):
    def __init__(self, nodes : Iterable[Node], values):
        self.Nodes = nodes
        self.Values = values
    def GetValue(self,x):
        return self.Values[0]*(self.Nodes[1].Position-x)/self.IntervalSize() + self.Values[1]*(x-self.Nodes[0].Position)/self.IntervalSize()
    def IntervalSize(self):
        return self.Nodes[1].Position - self.Nodes[0].Position