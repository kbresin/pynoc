class Vector(object):
    x = 0
    y = 0
    def __init__(self,x=0,y=0):
        self.x = float(x)
        self.y = float(y)
    def add(self, v):
        self.x += v.x
        self.y += v.y
    def pixels(self):
        return [int(self.x), int(self.y)]
    def copy(self):
        return Vector(self.x, self.y)
    def set(self, x, y):
        self.x = x
        self.y = y
    def coords(self):
        return(int(self.x), int(self.y))

#v1 = Vector(5,5)
#v2 = Vector(10,10)
#print(v1.x, v1.y)
#v1.add(v2)
#print(v1.x, v1.y)
