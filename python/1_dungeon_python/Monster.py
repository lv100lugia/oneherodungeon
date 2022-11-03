class Monster():
    def attack(self,hero):
        dmg=self.str//(hero.defence+hero.defenceDie)
        print(self.name + " attacks for " + str(dmg))
        hero.life -= dmg
        print ("hero life is now " + str(hero.life))
        
  

class Spider(Monster):
    def __init__(self):
        self.str = 4
        self.defence = 4
        self.life = 2
        self.range = 3
        self.move = 5
        self.name="Spider"
        


    def __str__(self):
        return(self.name + ": Life "  + str(self.life) + "\n "
               + str(self.move)    + " Move,  "
               + str(self.str)     + " Strength,  " 
               + str(self.defence) + " Defence,  " 
               + str(self.range)   + " Range "           
               )


        
class Skeleton(Monster):
    def __init__(self):
        self.str = 4
        self.defence = 5
        self.life = 3
        self.range = 4
        self.move = 4
        self.name="Skeleton"
        
        
    def __str__(self):
        return(self.name + ": Life "  + str(self.life) + "\n "
               + str(self.move)    + " Move,  "
               + str(self.str)     + " Strength,  " 
               + str(self.defence) + " Defence,  " 
               + str(self.range)   + " Range "           
               )

class Troll(Monster):
    def __init__(self):
        self.str = 7
        self.defence = 7
        self.life = 5
        self.range = 2
        self.move = 3
        self.name="Troll"
        
    def __str__(self):
        return(self.name + ": Life "  + str(self.life) + "\n "
               + str(self.move)    + " Move,  "
               + str(self.str)     + " Strength,  " 
               + str(self.defence) + " Defence,  " 
               + str(self.range)   + " Range "           
               )




class Dragon(Monster):
    def __init__(self):
        self.str = 5
        self.defence = 5
        self.life = 5
        self.range = 5
        self.move = 5
        self.name="Dragon"

    def __str__(self):
        return(self.name + ": Life "  + str(self.life) + "\n "
               + str(self.move)    + " Move,  "
               + str(self.str)     + " Strength,  " 
               + str(self.defence) + " Defence,  " 
               + str(self.range)   + " Range "           
               )


