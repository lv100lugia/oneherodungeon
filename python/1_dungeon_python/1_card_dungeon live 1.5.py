"""

1 card dungeon in pyhton

"""
import os
from Point import Point
from Hero import Hero
import Monster
from LevelBuilder import LevelBuilder

os.system('cls')
print("Welcome to 1 card dungeon")
rule=input("would you like to know the rules? (Y/N)")
if (rule+"N")[0].upper()=="Y": #den kigger på det først input med [0]
  print("At the start of every round you get 3 bonuce dice you can put. ")
  print("In your 3 stats Defence, attack or moment. Attack distance and moment")
  print("are both messured the same. Up, down, left and right count as 2 and")
  print("digonally counts as 3. after each level you level up and get 1 plus in")
  print("any of your 4 stats permanently or goes back to full health (6)")
  print("Damage is calulated by dividing attack with defence and rounding down")
  print("Fx 4 attack vs 4 defence does 1 dmg and 4 attack vs 5 defence does 0")
  print("and 6 attack vs 3 defence does 2 dmg")

lb=LevelBuilder()

hero = Hero()
print(hero)
level = 1
while level < 5 and hero.life>0:
  print("Level " + str(level))
  walls = lb.getWall(level)
  # For wall in walls:
  # Print (wall)
  monster = lb.getMonsterKind(level)
  monsterPoint = lb.monsterSpawn(level)
  heroPoint = lb.getStart(level)
  print(heroPoint)
  print(monsterPoint)
  print(monster)
 
  while monster.life>0 and hero.life>0:
      
    # Print map
    lb.printMap(heroPoint, monsterPoint)
    
    # Rolls and add bonus dice
    hero.buff()

    # Hero Move\/
    heromove_left=hero.move+hero.moveDie
    playerMove="yes"
    while heromove_left >= 2 and (playerMove+"N")[0].upper()=="Y":
    
        playerMove=input("Do you Want to move?(Y/N) ") 
        if (playerMove+"N")[0].upper()=="Y":
            print("NW  N  NE")
            print("  \ | /  ")
            print("W - * - E")
            print("  / | \  ")
            print("SW  S  SE")
            heroAction = input("Where do you want to move(" + str(heromove_left) + ")? ")

            x = 0
            y = 0
            if "W" in heroAction and heroPoint.x > 0:
              x = -1
            if "E" in heroAction and heroPoint.x < 4:
              x = +1
            if "S" in heroAction and heroPoint.y > 0:
              y = -1
            if "N" in heroAction and heroPoint.y < 4:
              y = +1 
              
            if heromove_left >= 3 and y * x != 0:
                heroPoint.x += x
                heroPoint.y += y
                heromove_left -= 3
                  
            else:
                if y == 0:
                    heroPoint.x += x
                else:
                    heroPoint.y += y
                heromove_left -= 2
            
        lb.printMap(heroPoint, monsterPoint)
    # Hero attack
    if heroPoint.inReach(monsterPoint,hero.range):
      hero.attack(monster)
    
    # Is monster alive
    if monster.life <= 0 :
      print("level clear gz")
      hero.level_up()
      level += 1
    else:
      
      # monster move
      monstermoment_left=monster.move

      while monsterPoint.isFar(heroPoint) and monstermoment_left >= 2:
        #monster wants to move to this direction 
        x = 0
        y = 0
        if monsterPoint.x > heroPoint.x:
          x = -1
        if monsterPoint.x < heroPoint.x:
          x = +1
        if monsterPoint.y > heroPoint.y:
          y = -1
        if monsterPoint.y < heroPoint.y:
          y = +1
          
        # moving the monster 
        if monstermoment_left >= 3 and y * x != 0:
          monsterPoint.x += x
          monsterPoint.y += y 
          monstermoment_left -= 3
          
        else:
          if y == 0:
            monsterPoint.x += x
          else:
            monsterPoint.y += y
          monstermoment_left -= 2
          
# monster attack
      if monsterPoint.inReach(heroPoint, monster.range):
        monster.attack(hero)

  
if hero.life<=0:
  print("you have no more health. r.i.p")
else:
  print("you survied the dungeon and killed all the monsters.")
