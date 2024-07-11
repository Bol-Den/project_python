
class Cars:

    def __init__(self, color, engine):
        self.color = color
        self.engine = engine

    def getColor(self):
        return self.color

    def getEngine(self):
        return self.engine

    def setNewColor(self,color):
        self.color = color