import random

class Hero:
    def __init__(self):
        self.life = 6
        self.range = 3
        self.str = 2
        self.strDie = 0 
        self.defence = 2
        self.defenceDie = 0
        self.move = 3
        self.moveDie = 0

        
    def __str__(self):
        return("Hero: Life "          + str(self.life)+ "\n "
               + str(self.move)       + " Move,  "
               + str(self.str)        + " Strength,  " 
               + str(self.defence)    + " Defence,  "
               + str(self.range)      + " Range\n+" 
               + str(self.moveDie)    + " Move, +" 
               + str(self.strDie)     + " Strength, +" 
               + str(self.defenceDie) + " Defence"    
               )

    
    def attack(self,monster):
        dmg=(self.strDie + self.str)//monster.defence
        print("Hero attacks for " + str(dmg))
        monster.life -= dmg
        print(monster.name + " life is now " + str(monster.life))

    def level_up(self):
        rule=""
        while rule !="L" and rule !="M" and rule !="S" and rule !="D" and rule !="R":
            rule=input("Do you want full (L)ife point or plus 1 in (M)ove, (S)trength, (D)efence or (R)ange(L/M/S/D/R)")
            rule=rule.upper()
            
        match rule:
            case "L":
                self.life=6
                print("you have now 6 life again")
            case "M":
                self.move=self.move+1
                print("you now have " + str(self.move))
            case "S":
                self.str=self.str+1
                print("you now have " + str(self.str))
            case "D":
                self.defence=self.defence+1
                print("you now have " + str(self.defence))
            case "R":
                self.range=self.range+1
                print("you now have " + str(self.range))

    def buff(self):
        #slå 3 D6
        
        d6_1 = random.randrange(1,7)
        d6_2 = random.randrange(1,7)
        d6_3 = random.randrange(1,7)
        
        #give buffs til Move, stergth eller defence
        
        self.strDie = 0
        self.defenceDie = 0
        self.moveDie = 0

        
        aprove = "N"
        while aprove.upper()!= "Y":
            print("The dice rolled")
            print(d6_1, d6_2, d6_3)
            
            dice = "xxx"
            while len(dice)!=3 or "M" not in dice or "S" not in dice or "D" not in dice: 
                dice = input("where do you want the buff dice to go (M)ove, (S)trength, (D)efence)")
                dice = dice.upper()
                
            self.setDie(dice[0], d6_1)
            self.setDie(dice[1], d6_2)
            self.setDie(dice[2], d6_3)
            print(self)
            aprove = input("are you sure(Y/N)")
       

        
    def setDie(self,die_letter,die): 
        if die_letter=="S":
            self.strDie=die
        elif die_letter=="D":
            self.defenceDie=die
        elif die_letter=="M":
            self.moveDie=die







        
