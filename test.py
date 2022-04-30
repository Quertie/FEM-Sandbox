from Meshing.Meshing import Node
from Approximation import PiecewiseLinearInterpolator

nodes = [Node(i*0.2, i) for i in range(0,6)]
f = lambda x : x*x

f = PiecewiseLinearInterpolator.CreateFromNodes(f, nodes)
