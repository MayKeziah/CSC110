#sphere class
import math
class sphere:
    def __init__(self, Radius):
        self.radius = Radius
    def getRaduis(self):
        return self.radius
    def surfaceArea(self):
        return 4*math.pi*(self.radius)**2
    def volume(self):
        return (4/3)*math.pi*(self.radius**3
