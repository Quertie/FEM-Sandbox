from typing import Callable, Iterable
from Approximation.Function import Function
from Approximation.LinearInterpolator import LinearInterpolator
from Meshing.Meshing import Mesh
from Meshing.Node import Node

class PiecewiseLinearInterpolator(Function):
    def __init__(self, nodes : Iterable[Node], values):
        self.Mesh = Mesh.CreateElements(nodes)
        self.Pieces = dict([(self.Mesh.Elements[i], LinearInterpolator(self.Mesh.Elements[i].Nodes, (values[i], values[i+1]))) for i in range (len(self.Mesh.Elements))])
    def GetValue(self, x):
        element = self.Mesh.GetElementForPosition(x)
        return self.Pieces[element].GetValue(x)

    @classmethod
    def CreateFromNodes(cls, f : Callable[[float], float], nodes : Iterable[Node]):
        instance = cls(nodes, [f(node.Position) for node in nodes])
        return instance