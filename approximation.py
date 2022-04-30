import Meshing

class Function:
    def GetValue(self,x):
        return 1 #override this

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
        self.Mesh = PiecewiseLinearInterpolator.CreateElements(nodes)
        self.Pieces = dict([(self.Mesh.Elements[i], LinearInterpolator(self.Mesh.Elements[i].Nodes, (values[i], values[i+1]))) for i in range (len(self.Mesh.Elements))])
    def CreateElements(nodes):
        return Meshing.Mesh([Meshing.Element([nodes[i], nodes[i+1]]) for i in range(len(nodes)-1)])
        
    
