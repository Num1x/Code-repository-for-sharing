import time
import random

ogreHitPoints = 10
ogreArmorClass = 12
ogreAlive = 1
equippedWeapon = "Starter Sword"
starterSwordMaxDamage = 8
equippedArmor = "Starter Armor"
StarterArmorClass = 12
ogreDaggerMax = 6
playerHealth = 20

characterLifestyle = None
lifestyleChosen = None

def Cprint(text,t):
    Ltext=list(text)
    for i in range(0,len(Ltext)-1):
        print(Ltext[i],end='')
        time.sleep(t)
    print(Ltext[len(Ltext)-1])

Cprint("Welcome to Five Coffee Cups! When you are ready to play please type continue",0.1)
time.sleep(1)
readyOrNot = input()
if readyOrNot == "debug":
  ogreHitPoints = 1
  Cprint('Debug mode activated',0.1)
  Cprint("Welcome to Five Coffee Cups!",0.1)
  readyOrNot = 'continue'

if readyOrNot == "continue":
    Cprint("Welcome to the tutorial, you will be fighting an ogre. This is what a fight will look like while you are playing the game.",0.1)
    ogreAlive = 1
    time.sleep(1)
    while True:
        Cprint("Type attack to engage your enemy",0.1)
        attackChoice = input()
        if attackChoice == "attack":
            Cprint("rolling d20 for attack roll",0.1)
            randomRoll = random.randint(1,20)
            if randomRoll >= ogreArmorClass:
                Cprint("You have successfully hit the ogre with your " + equippedWeapon + " with a roll of:",0.1)
                time.sleep(1)
                print(randomRoll)
                damageDealt = random.randint(1,starterSwordMaxDamage)
                Cprint("You have dealt",0.1)
                time.sleep(1)
                print(damageDealt)
                time.sleep(1)
                Cprint("to the ogre!",0.1)
                ogreHitPoints = ogreHitPoints - damageDealt
                if ogreHitPoints <= 0:
                    ogreAlive = 0
            else:
                time.sleep(1)
                Cprint("You have missed the ogre with a roll of:",0.1)
                time.sleep(1)
                print(randomRoll)
            if ogreAlive == 1:
                Cprint("Now the ogre will attempt to attack you",0.1)
                time.sleep(1)
                ogreAttack = random.randint(1,20)
                if ogreAttack >= StarterArmorClass:
                    damageDealt = random.randint(1,ogreDaggerMax)
                    Cprint("The ogre has successfully attacked you and dealt",0.1)
                    time.sleep(1)
                    print(damageDealt)
                    time.sleep(1)
                    Cprint("damage",0.1)
                    time.sleep(1)
                    playerHealth = playerHealth - damageDealt
                else:
                    time.sleep(1)
                    Cprint("The ogre has missed you with a roll of",0.1)
                    time.sleep(1)
                    print(ogreAttack)
                    time.sleep(2)
                Cprint("You now have ",0.1)
                time.sleep(1)
                print(playerHealth)
                time.sleep(1)
                Cprint("health left",0.1)
                time.sleep(1)
                print("")
                Cprint("The ogre now has",0.1)
                time.sleep(1)
                print(ogreHitPoints)
                time.sleep(1)
                Cprint("health left",0.1)
                print("")
                time.sleep(2)
            else:
                ogreAlive = 0
        if ogreAlive == 0:
            Cprint("You have killed the ogre!",0.1)
            break
    Cprint("Great job! You have successfully finished the tutorial!",0.1)
    print("")
    x = 1
    for x in "bananananananananananananananananananananananananananananananananananananananananananananananana monke pog":
      print("")
    Cprint("Which character lifestyle do you want to choose",0.1)
    Cprint("Your lifestyle choices:",0.1)
    Cprint("Ginger(soul sucker), Felix(crazed gencidal maniac)",0.1)          
    characterLifestyle = input()
    if characterLifestyle == "Felix":
        Cprint("You have selected the lifestyle Felix. This means you are a crazed genocidal maniac which gives you a bonus + 2 on damage rolls.",0.1)
        lifestyleChosen = 'yes'
    if characterLifestyle == "Ginger":
        Cprint("You have selected the lifestyle Ginger. This means you can suck peoples souls which gives you a +5 to hit an enemy.",0.1)
        lifestyleChosen = 'yes'
    if lifestyleChosen == "None":
        Cprint("You have not selected a valid lifestyle, please select a valid lifestyle",0.1)

    x = 1
    Cprint("The Game will now begin...",0.1)
    for x in "bananananananananananananananananananananananananananananananananananananananananananananananana monke pog":
      print("")
    
    def attackEnemy(enemy):
      Cprint('You have encountered a ' + enemy,0.1)
      enemy = enemy.lower()
      if enemy == 'monke':
        Cprint("You have been brutally banana'd by the monke, you ded",0.1)
        raise Exception('YOU HAVE BEEN BANANA\'D BY THE MONKE')
      if enemy == 'ogre':
        print("Are you ready to attack the " + enemy + "?")
      if enemy == 't-rex':
        print("Are you ready to attack the " + enemy + "?")
      if enemy == 'humongous frog':
        print("Are you ready to attack the " + enemy + "?")
      if enemy == 'goblin':
        print("Are you ready to attack the " + enemy + "?")
      if enemy == 'david':
        print("Are you ready to attack the " + enemy + "?")
      if enemy == 'felix':
        print("Are you ready to attack the " + enemy + "?")
      if enemy == 'harpy':
        print("Are you ready to attack the " + enemy + "?")
  
    enemy1 = input()
    
    attackEnemy(enemy1)




























































    x = 1
    for x in "bananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananannananananananananananananananananaanannananaannanaanannananananananananananananananananananananananananananananannaananananananananananananananananananananaanananananananananannnnnnnnnanananananananananannnnnnnanaananannananananananananananan monke pog":
      print("")
