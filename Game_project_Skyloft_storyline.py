#Skyloft Sword storyline
#After beginning
import time
import random
#importied input funtions available. Do not copy over.
t = None #used
u = None #used
v = None #used
w = None #used
x = None #used
y = None #used
z = None #used
#raise Exception("haha you got screwed over noob.")

#Imported funtions(don't transfer to main file)
#printing function
def Cprint(text,t=0.03):
    Ltext=list(text)
    for i in range(0,len(Ltext)-1):
        print(Ltext[i],end='')
        time.sleep(t)
    print(Ltext[len(Ltext)-1])
#combat function
def combat(weapon, enemy):
  if enemy == "Shark":
      echance = random.randint(3,5)
  if enemy == "Merperson":
      echance = random.randint(3,6)
  if enemy == "Goblin":
    echance = random.randint(1,4)
  if enemy == "Orc":
    echance = random.randint(2, 5)
  if enemy == "Human Fighter":
    echance = random.randint(3,6)
  if enemy == "Wizard":
    echance = random.randint(5,8)
  if enemy == "Dragon":
    echance = random.randint(9,12)
  if enemy == "Mage":
    echance = random.randint(4,7)
  if enemy == "Sorcerer":
    echance = random.randint(9,12)
  if weapon == "Dagger" :
    pchance = random.randint(3,6)
  if weapon == "Sword":
    pchance = random.randint(4,7)
  if weapon == "Staff":
    pchance = random.randint(6,9)
  if weapon == "Wand":
    pchance = random.randint(5,8)
  if weapon == "Sword 2":
    pchance = random.randint(4,7)
  if weapon == "Sword 3":
    pchance = random.randint(5,8)
  if weapon == "Bow":
    pchance = random.randint(3,6)
  if weapon == "Bow 2":
    pchance = random.randint(4,7)
  if weapon == "Bow 3":
    pchance = random.randint(5,8)
  if weapon == "Crossbow":
    pchance = random.randint(4,7)
  if weapon == "Crossbow 2":
    pchance = random.randint(5,8)
  if weapon == "Crossbow 3":
    pchance = random.randint(6,8)
  if weapon == "Staff 2":
    pchance = random.randint(7,10)
  if weapon == "Staff 3":
    pchance = random.randint(8,11)
  if weapon == "Wand 2":
    pchance = random.randint(6,9)
  if weapon == "Wand 3":
    pchance = random.randint(7,10)
  if weapon == "Dagger 2":
    pchance = random.randint(4,7)
  if weapon == "Dagger 3":
    pchance = random.randint(5,8)
  if pchance > echance:
    Cprint("You are victorious!")
    cont = True
  if echance > pchance:
    Cprint("You are defeated!")
    cont = False
  if pchance == echance:
    Cprint("You sustain heavy losses but win!")
    cont = True
#don't copy over
inventory = ["Dagger", "Bow and arrows", "Wand", "Sword 2", "Gold: 50"]

#Beginning of Storyline
cont = True
while cont:
    Cprint("With your new tools and knowledge in hand, you set out on your journey.")
    time.sleep(0.5)
    Cprint("You find your self on the banks of the Lake, on the Northern shore near the town.")
    time.sleep(1)
    Cprint("Your map tells you to head down to the middle of lake.")
    time.sleep(1)
    Cprint("But you do not know how, you cannot hold your breath that long, and there are no submarines.")
    time.sleep(1)
    Cprint("Do you want to A: try to make it to the bottom of the lake on your own or B: Consult the book for more information?")
    t = input()
    t = t.lower()
    if t == "a":
        Cprint("You attempt to swim to the middle bottom of the lake, but die in the process")
        time.sleep(1)
        Cprint("You find yourself back on the Norther shore of the lake.")
    time.sleep(1)
    Cprint("In the book you find new instructions appeared.")
    time.sleep(0.5)
    Cprint("It gives you a temporary water breating spell you can use with a few simple ingredients.")
    time.sleep(1)
    Cprint("The ingredients are: ")
    time.sleep(0.4)
    Cprint("-Water of a lake.")
    time.sleep(0.3)
    Cprint("-Soil of the banks of the lake.")
    time.sleep(0.4)
    Cprint("-And leaves of a tree who's roots take the water of the lake.")
    time.sleep(0.4)
    Cprint("You notice that you can find all of these ingredients near you.")
    time.sleep(0.5)
    Cprint("Which would you like to collect first? A: Leaves of the tree, B: Water of the Lake or C: the soil of the bank?")
    u = input()
    u = u.lower()
    if u == "a":
        Cprint("You collect the leaves of a nearby oak tree.")
    if u == "b":
        Cprint("You collect water from the lake.")
    if u == "c":
        Cprint("You collect the soil of the bank.")
    Cprint("Now that you have all the ingredients, the book tells you to mix them in a hole in the dry ground, and stick your head in it.")
    time.sleep(1)
    Cprint("You feel a bubble form around your head after you stick your head in the whole.")
    time.sleep(0.5)
    Cprint("Now you are ready to head into the lake.")
    time.sleep(0.5)
    Cprint("You enter the lake and soon find it is an entirely different world under the surface.")
    time.sleep(1)
    Cprint("The book begins to glow and soon a path to the middle of the lake is visible.")
    time.sleep(0.8)
    Cprint("You catch a glimplse of your first enemy.")
    time.sleep(0.5)
    Cprint("You find that it is a merman holding a spiked trident.")
    time.sleep(1)
    Cprint("You have no choice but to fight, or die trying!")
    time.sleep(0.5)
    Cprint("Here is your inventory: ")
    print(inventory)
    time.sleep(1)
    Cprint("Which weapon would you like to use? ")
    u = input()
    if u == "Sword 2" or u == "sword 2" or u == "sword2" or u == "Sword2":
        Cprint("You choose your level 2 sword!")
        hand = "Sword 2"
    elif u == "Dagger" or u == "dagger":
        Cprint("You chose your level 2 sword!")
        hand = "Dagger"
    elif u == "Wand" or u == "wand":
        Cprint("You chose your wand!")
        hand = "Wand"
    elif u == "Bow" or u == "bow" or u == "Bow and arrows" or u == "bow and arrows":
        Cprint("You chose your bow and arrows!")
        hand = "Bow"
    else:
        print("That is not an acceptable answer. restart the game.")
        break
    time.sleep(1)
    Cprint("It is now time to fight! To prove your worth, and pass your first combat challenge!")
    combat(hand, "Merperson")
    if cont == False :
        Cprint("You are unfortunately defeated and are forced to start again.")
        break
    if cont == True :
        Cprint("You are victorious and continue on your journey!")
        pass
    time.sleep(0.5)
    Cprint("You continue towards the middle of the lake and then you see them.")
    time.sleep(1)
    Cprint("Three sharks circling around a massive structure that appears to be a coral pallace.")
    time.sleep(2)
    Cprint("You will have no choice but to fight your way through at least two of them.")
    time.sleep(1.5)
    Cprint("To fight them all you may want to use some magic from your wand.")
    time.sleep(1)
    Cprint("Here is your invnetory again")
    time.sleep(0.5)
    print(inventory)
    time.sleep(1)
    Cprint("Which weapon do you wish to use? Keep in mind my suggestion.")
    v = input()
    v.lower()
    if v == "Sword 2" or v == "sword 2" or v == "sword2" or v == "Sword2":
        Cprint("You choose your level 2 sword!")
        hand = "Sword 2"
    elif v == "Dagger" or v == "dagger":
        Cprint("You chose your level 2 sword!")
        hand = "Dagger"
    elif v == "Wand" or v == "wand":
        Cprint("You chose your wand!")
        time.sleep(0.5)
        Cprint("As you grab the wand a spell to blast enemies pops up in your head.")
        time.sleep(1.5)
        hand = "Wand"
    elif v == "Bow" or v == "bow" or v == "Bow and arrows" or v == "bow and arrows":
        Cprint("You chose your bow and arrows!")
        hand = "Bow"
    time.sleep(0.5)
    Cprint("It is now time to battle.")
    time.sleep(0.5)
    combat(hand, "Shark")
    if cont == True:
        Cprint("Congratulations! You are successful at vanquishing your enemies!")
        pass
    elif cont == False:
        Cprint("You are not successful, but recieve another chance.")
        time.sleep(0.5)
        combat(hand, "Shark")
        if cont == True:
            Cprint("Congratulations! You are successful at vanquishing your enemies!")
            pass
        elif cont == False:
            Cprint("You are not successful, and must restart.")
            continue
    Cprint("You find a giant doorway at the base of the corral pallace.")
    time.sleep(1)
    Cprint("There is a big blue spot in the middle of the doorway. Do you wish to push it?")
    w = input()
    w = w.lower()
    time.sleep(0.5)
    if w == "yes" or w == "y":
        Cprint("You press the blue spot.")
        time.sleep(0.3)
        pass
    elif w == "no" or w == "n":
        Cprint("Do you wish to try and push another spot?")
        x = input()
        x = x.lower()
        if x == "yes" or x == "y":
            Cprint("")
        elif x == "no" or x == "n":
            pass
    Cprint("The blue spot lights up and the doors swing open.")
    time.sleep(0.4)
    Cprint("You see the inside of the building.")
    time.sleep(0.4)
    Cprint("There is a stair passageway leading upwards.")
    time.sleep(0.4)
    Cprint("At the top of it you find the undead sorcerer.")
    time.sleep(0.4)
    Cprint("You find that he seems to be sleeping.")
    time.sleep(0.3)
    Cprint("Then you see it.")
    time.sleep(0.4)
    Cprint("A blue stone that is glowing. Incased in a blueish white sphere of magic.")
    time.sleep(1.5)
    Cprint("Do you A: rush towards it or B: Wait?")
    y = input()
    y = y.lower()
    if y == "a":
        Cprint("You rush towards the sphere and then the sorcerer wakes up.")
        time.sleep(1)
        Cprint("You now must fight the sorcerer.")
        time.sleep(0.5)
        Cprint("Here is your inventory: ")
        print(inventory)
        time.sleep(1)
        Cprint("Which weapon would you like to use?")
        ab = input()
        ab = ab.lower()
        if ab == "Sword 2" or ab == "sword 2" or ab == "sword2" or ab == "Sword2":
            Cprint("You choose your level 2 sword!")
            hand = "Sword 2"
        elif ab == "Dagger" or ab == "dagger":
            Cprint("You chose your level 2 sword!")
            hand = "Dagger"
        elif ab == "Wand" or ab == "wand":
            Cprint("You chose your wand!")
            time.sleep(0.5)
            hand = "Wand"
        elif ab == "Bow" or ab == "bow" or ab == "Bow and arrows" or ab == "bow and arrows":
            Cprint("You chose your bow and arrows!")
            hand = "Bow"
        time.sleep(1)
        Cprint("You will get three attempts to fight the sorcerer, win one and you win the battle.")
        time.sleep(2)
        for count in 3:
            combat(hand, "Sorcerer")
            if cont == True:
                break
            elif cont == False:
                pass
        if cont == True:
            time.sleep(1)
            Cprint("You see the blue sphere is gone.")
            time.sleep(0.5)
            Cprint("You walk up to the stone and take it.")
        elif cont == False:
            time.sleep(1)
            Cprint("You are forced to restart.")
            break
    elif y == "b":
        Cprint("You wait back. Do you A: cast a your blasting spell at the sorcerer, or B: Cast your spell at the sphere?")
        z = input()
        z = z.lower()
        if z == "a":
            Cprint("The sorcerer dissolves in front of you and the shpere around the stone dissapears.")
            time.sleep(2)
        elif z == "b":
            Cprint("The shpere is unaffected, and the sorcerer wakes up.")
            time.sleep(1)
            Cprint("You know must fight the sorcerer.")
            time.sleep(0.5)
            Cprint("Here is your inventory: ")
            print(inventory)
            time.sleep(1)
            Cprint("Which item would you like to use?")
            ah = input()
            ah = ah.lower()
            if ah == "Sword 2" or ah == "sword 2" or ah == "sword2" or ah == "Sword2":
                Cprint("You choose your level 2 sword!")
                hand = "Sword 2"
            elif ah == "Dagger" or ah == "dagger":
                Cprint("You chose your level 2 sword!")
                hand = "Dagger"
            elif ah == "Wand" or ah == "wand":
                Cprint("You chose your wand!")
                time.sleep(0.5)
                hand = "Wand"
            elif ah == "Bow" or ah == "bow" or ah == "Bow and arrows" or ah == "bow and arrows":
                Cprint("You chose your bow and arrows!")
                hand = "Bow"
            time.sleep(1)
            Cprint("You will get three attempts to fight the sorcerer, win one and you win the battle.")
            time.sleep(2)
            for count in 3:
                combat(hand, "Sorcerer")
                if cont == True:
                    break
                elif cont == False:
                    pass
            if cont == True:
                time.sleep(1)
                Cprint("You see the blue sphere is gone.")
                time.sleep(0.5)
                Cprint("You walk up to the stone and take it.")
            elif cont == False:
                time.sleep(1)
                Cprint("You are forced to restart.")
                break
    time.sleep(1)
    Cprint("You now have the sphere and have passed the first part of this game.")
    time.sleep(1)
    while True:
        time.sleep(1)
        Cprint("You have now made it to the second part.")
        time.sleep(0.5)
        Cprint("You have teleported to a floating island.")
        time.sleep(0.5)
        Cprint("You look around and you see multiple islands connected by various bridges.")
        time.sleep(1)
        Cprint("The stone begins to glow and you see one of the islads is suddenly outlined in blue.")
        time.sleep(1.5)
        Cprint("You see that there are 2 islands between the island you are currently on and the one outlined in blue.")
        time.sleep(2)
        Cprint("Each seems to have some orcs on it that you will need to fight")
        time.sleep(1)
        Cprint("Do you want to continue?")
        eh = input()
        eh = eh.lower()
        if eh == "yes" or eh == "y":
            Cprint("You continue to the first islands.")

        elif eh == "no" or eh == "n":
            Cprint("What would you like to do instead?")

        Cprint("The first island has an orc guarding the bridge to get to it.")
        time.sleep(1)
        Cprint("You now must fight it.")
        time.sleep(1)
        Cprint("Here is your inventory, which weapon would you like to use?")
        print(inventory)
        uh = input()
        uh = uh.lower()
        if uh == "dagger":
            Cprint("you choose a dagger!")
            hand = "Dagger"

        elif uh == "sword 2" or uh == "sword2":
            Cprint("You choose your level 2 sword!")
            hand = "Dagger"

        elif uh == "bow":
            Cprint("You choose your bow and arrows!")
            hand = "Bow"

        elif "bow" in uh:
            Cprint("You choose your bow and arrows!")
            hand = "Bow"
        elif uh == "wand":
            Cprint("You choose your wand!")
            hand = "Wand"

        combat(hand,"Orc")
        
            

    break
    
        
        
        
            
        
    



