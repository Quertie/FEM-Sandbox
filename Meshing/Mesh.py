from typing import Iterable
from Meshing.Elements import Element
from Meshing.Node import Node


class Mesh:
    def __init__(self, elements : Iterable[Element]):
        self.Elements = elements

    def CreateElements(nodes : Iterable[Node]):
        return Mesh([Element([nodes[i], nodes[i+1]]) for i in range(len(nodes)-1)])

    def GetElementForPosition(self, x : float):
        for element in self.Elements:
            if element.Contains(x): return element