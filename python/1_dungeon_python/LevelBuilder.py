from Point import Point
from Monster import *

class LevelBuilder:
    def getWall(self, level):
        if(level % 4 == 1):
            wall1 = Point(1,1)
            wall2 = Point(3,1)
            wall3 = Point(3,3)
            return [wall1,wall2,wall3]
          
        if(level % 4 == 2):
            wall1 = Point(4,1)
            wall2 = Point(4,2)
            wall3 = Point(0,2)
            return [wall1,wall2,wall3]

        if(level % 4 == 3):
            wall1 = Point(1,1)
            wall2 = Point(1,3)
            wall3 = Point(3,3)
            return [wall1,wall2,wall3]


        if(level % 4 == 0):
            wall1 = Point(5,2)
            wall2 = Point(1,2)
            wall3 = Point(1,3)
            return [wall1,wall2,wall3]

        
    def getMonsterKind(self, level):
        if(level % 4 == 1):
            return Spider()
        
        if(level % 4 == 2):
            return Skeleton()
        
        if(level % 4 == 3):
            return Troll()
        
        if(level % 4 == 0):
            return Dragon()
            
    def getStart(self, level):
        if(level % 2 == 1):
            return Point(0,0)
        else:
            return Point(4,0)


    def monsterSpawn(self, level):
        if level == 1:
            return Point(4,4)
        if level == 2:
            return Point(0,3)
        if level == 3:
            return Point(4,3)
        if level == 4:
            return Point(1,4)
        else:
            return Point(2,2)


    def printMap(self, heroPoint, monsterPoint):
        print("-----------------------------")
        for y in range(4, -1, -1):
            maprow = ""
            for x in range(5):
                if x == heroPoint.x and y == heroPoint.y:
                    maprow += " H   "
                elif x == monsterPoint.x and y == monsterPoint.y:
                    maprow += " M   "
                else:
                    maprow += str(x) + "," + str(y) + "  " 
            print("|  " + maprow + "|")
        print("-----------------------------") 

            
            
















        
    
    
