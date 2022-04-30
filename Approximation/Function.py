class Function:
    def GetValue(self,x):
        return 1 #override this
    def AsDelegate(self):
        return lambda x: self.GetValue(x)