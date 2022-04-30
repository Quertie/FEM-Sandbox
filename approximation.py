from Meshing import Mesh

class Function:
    def GetValue(self,x):
        return 1 #override this
    def AsDelegate(self):
        return lambda x: self.GetValue(x)

class LinearInterpolator(Function):
    def __init__(self, nodes, values):
        self.Nodes = nodes
        self.Values = values
    def GetValue(self,x):
        return self.Values[0]*(self.Nodes[1].Position-x)/self.IntervalSize() + self.Values[1]*(x-self.Nodes[0].Position)/self.IntervalSize()
    def IntervalSize(self):
        return self.Nodes[1].Position - self.Nodes[0].Position

class PiecewiseLinearInterpolator(Function):
    def __init__(self, nodes, values):
        self.Mesh = Mesh.CreateElements(nodes)
        self.Pieces = dict([(self.Mesh.Elements[i], LinearInterpolator(self.Mesh.Elements[i].Nodes, (values[i], values[i+1]))) for i in range (len(self.Mesh.Elements))])
    def GetValue(self, x):
        element = self.Mesh.GetElementForPosition(x)
        return self.Pieces[element].GetValue(x)

    @classmethod
    def CreateFromNodes(cls, f, nodes):
        instance = cls(nodes, [f(node.Position) for node in nodes])
        return instance