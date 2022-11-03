"""

1 card dungeon in pyhton

"""
print("Welcome to 1 card dungeon")
rule=input("would you like to know the rules? (Y/N)")
if (rule+"N")[0].upper()=="Y": #den kigger på det først input med [0]
  print("exsample text exe")
  print("exsample text exe")
  print("exsample text exe")
  print("exsample text exe")
  print("exsample text exe")




life=6
level = 1
while level < 6 and life>0:
  print("Level " + str(level))

  monster_alive=True
  while monster_alive and life>0:
    win=input("did you kill the monster?(Y/N)")
    if (win+"N")[0].upper()=="Y":
      monster_alive=False
      print("gz")
      level += 1
    else:
      life -= 1
      print("you loss a life. Now you have " + str(life))
  
if life==0:
  print("you have no more health. r.i.p")
else:
  print("you survied the dungeon and killed all the zmonsters.")
