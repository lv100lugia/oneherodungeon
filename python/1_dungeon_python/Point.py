class Point:
    def __init__(self, x,y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return str(self.x) + "," + str(self.y)


    def isFar(self,point):
        return(self.x-point.x)**2 + (self.y-point.y)**2 > 2

    def inReach(self,point,reach):
        dist = 0
        if reach == 2:
            dist = 1
        if reach == 3:
            dist = 2
        if reach == 4:
            dist = 4
        if reach == 5:
            dist = 5
        if reach == 6:
            dist = 8
        return(self.x-point.x)**2 + (self.y-point.y)**2 <= dist
    
    
        
