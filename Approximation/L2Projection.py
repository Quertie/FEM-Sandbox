from typing import Callable, Iterable
from Approximation.PiecewiseLinearFunction import PiecewiseLinearFunction
from Meshing.Elements import Element, LinearElement
from Meshing.Node import Node
from numpy import zeros, array, matmul
from numpy.linalg import inv

class L2Projection(PiecewiseLinearFunction):
    @classmethod
    def InterpolateFromNodes(cls, f : Callable[[float], float], nodes : Iterable[Node]):
        n = len(nodes)
        massMatrix = cls.__ComputeMassMatrix(nodes)
        loadVector = cls.__ComputeLoadVector(f, nodes)

        solutionVector = matmul(inv(massMatrix), loadVector)

        return PiecewiseLinearFunction(nodes, solutionVector.transpose().tolist()[0])

    @classmethod
    def __ComputeMassMatrix(cls, nodes : Iterable[Node]):
        n = len(nodes)
        massMatrix = zeros([n, n])
        for i in range(n-1):
            e = LinearElement([nodes[i], nodes[i+1]])
            massMatrix[i : i+2, i:i+2] += e.MassMatrix
        return massMatrix
    
    @classmethod
    def __ComputeLoadVector(cls, f, nodes : Iterable[Node]):
        n = len(nodes)
        loadVector = zeros([n, 1])
        for i in range(n-1):
            e = LinearElement([nodes[i], nodes[i+1]])
            # Using trapezoidal quadrature
            loadVector[i:i+2] += 0.5 * array([[f(nodes[i].Position)], [f(nodes[i+1].Position)]]) * e.IntervalSize
        return loadVector