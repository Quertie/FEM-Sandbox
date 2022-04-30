import Meshing
import approximation

n1 = Meshing.Node(0,0)
n2 = Meshing.Node(1,1)

nodes = (n1,n2)
values = (0,1)

f = approximation.PiecewiseLinearInterpolator(nodes, values)

print(f.GetValue(0.5))
