from Meshing.Node import Node
from Approximation.L2Projection import L2Projection
from matplotlib import pyplot as plt

nodes = [Node(i*0.2, i) for i in range(0,6)]
f = lambda x : x*x

a = L2Projection.InterpolateFromNodes(f, nodes).AsDelegate()

xspace = [i/100 for i in range(101)]
plt.figure(1)
plt.plot(xspace, [f(x) for x in xspace])
plt.plot(xspace, [a(x) for x in xspace])
plt.show()
