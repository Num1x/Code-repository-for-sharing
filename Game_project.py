import time
import random
#Input variables:
a = None #Used
b = None #used
c = None #used
d = None #used
e = None #used
f = None #used
g = None #used
h = None #used
i = None #used
j = None #used
k = None #used
l = None #used
m = None #used
n = None #used
o = None #used
p = None #used
q = None #used
r = None #used
s = None #used
#For Skyloft Sword Storyline
t = None
u = None
v = None
w = None
x = None
y = None
z = None

#printing function
def Cprint(text,t=0.03):
    Ltext=list(text)
    for i in range(0,len(Ltext)-1):
        print(Ltext[i],end='')
        time.sleep(t)
    print(Ltext[len(Ltext)-1])
#combat function
def combat(weapon, enemy):
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
  if echance > pchance:
    Cprint("You are defeated!")
  if pchance == echance:
    Cprint("You sustain heavy losses but win!")

inventory = ["Dagger", "Bow and arrows", "Wand"]
str_inventory = str(inventory)
gameplay = True #Indicates wheather game is running.
while gameplay :
  #intro
  Cprint("Welcome to the adventures of Chad Bodeman!")
  time.sleep(1)
  Cprint("To begin please choose an adventure.")
  time.sleep(1)
  Cprint("Your options are: a Forrest Dragon, b Mountain Treasure, and c Skyloft Sword. Please enter the letter of the adventure you would like to do below.")
  a = input()
  a = a.lower()
  time.sleep(0.25)

  #Forrest Dragon story line:
  if a == "a":
    Cprint("You chose Forrest Dragon!")
    time.sleep(0.75)
    Cprint("Let the adventure begin!")
    time.sleep(1.5)
    Cprint("You are on the edge of the forrest of dean. In the village of Eregion. Nearby is a tavern where you can find directions, and information about the dragon that lies deep within the forrest. Defeating the dragon is said to give you power beyond your imagination. Do you want to go to the tavern?")
    b = input()
    b = b.lower()
    time.sleep(0.25)
    if b == "yes":
      Cprint("You enter the tavern.")
    elif b == "no":
      Cprint("You do not enter the tavern")
      Cprint("Do you want to go to the woods now?")
      c = input()
      c = c.lower()
      if c == "yes" :
        Cprint("You enter the forrest.")
      elif c == "no" :
        Cprint("Do you want to go to the tavern?")
        d = input()
        d = d.lower()
        if d == "yes":
          Cprint("You go to the tavern")
        elif d == "no":
          Cprint("restart the game.")
          gameplay = False

#Mountain Treasure story line:
  elif a == "b":
    Cprint("You chose Mountain Treasure!")
    Cprint("Let the adventure begin!")
    Cprint("You begin in the foothills of the Iron Mountains, in the town of Dale.")
    Cprint("In the town, there is an old traveler, who happens to be in town now. You hear from the locals that he knows more about the mountains and their treasure than anyone. Do you go to him?")
    e = input()
    e = e.lower()
    if e == "yes":
      Cprint("You visit the traveler.")
    elif e == "no":
      Cprint("Do you wish to go into the mountains now?")
      f = input()
      f = f.lower()
      if f == "yes":
        Cprint("You go into the mountain.")
      elif f == "no":
        Cprint("Would you like to visit the weapons shop?")
        g = input()
        g = g.lower()
        if g == "yes":
          Cprint("You go to the weapons shop ryder was here.")
        elif g == "no":
          Cprint("Restart the game.")
          gameplay = False

#Skyloft Sword Storyline
  elif a == "c":
    #intro and lore
    Cprint("You chose Skyloft Sword")
    time.sleep(1.5)
    Cprint("Let the adventure begin!")
    time.sleep(1.5)
    Cprint("You start in the major city of Lake Town")
    time.sleep(1.5)
    Cprint("The city of Lake Town is known for a great old legend.")
    time.sleep(1.5)
    Cprint("It is known as the sacred point where the people of old left this world. They are said to have taken chunks out of Earth, which turned into the Skyloft islands. The crater left by these chunks being taken out formed the lake on which Laketown sits. It is said the skyloft islands are hidden from the eyes of those who dwell on land. To reach the islands, there is said to be a sacred stone, found deep within the lake, that will show you the path.")
    time.sleep(1)
    print("")
    time.sleep(1)
    Cprint("bum bum bum!!!")
    time.sleep(1.5)
    #Sage introduction:
    Cprint("In Lake Town, there is an old Shaman who is fabled to be the last living descendant of the people of old. He may know information about the stone you seek. Do you wish to go to him?")
    h = input()
    h = h.lower()
    if h == "yes":
      Cprint("You set out to find the Shaman!")
      time.sleep(0.5)
      Cprint("The Shaman lives in a hut on the outskirts of the town. To get there you will need directions. Do you wish to ask a passing person?")
      k = input()
      k = k.lower()
      if k == "yes":
        #First interaction
        Cprint("You ask a person walking by. She tells you to head South down the main road, which you are currently on. She then says,'Take a right at the road called amber road, and you will see his hut.'")

      elif k == "no":
        Cprint("Do you wish to find him on your own?")
        l = input()
        l = l.lower()
        if l == "yes":
          Cprint("You set off around town.")
        if l == "no":
          Cprint("Do you wish to go to the tavern to find out?")
          m = input()
          m = m.lower()
          if m == "yes":
            Cprint("You go to the tavern.")

          elif m == "no":
            Cprint("Please restart the game.")
            gameplay = False
    if h == "no":
      Cprint("Would you like to visit the old library which contains tales of old?")
      i = input()
      i = i.lower()
      if i == "yes" :
        Cprint("You enter the library!")
        time.sleep(0.5)
        Cprint("In the library there is a section on history.")
        time.sleep(0.5)
        Cprint("There is also a section on magic")
        time.sleep(0.5)
        Cprint("Which one would you like to visit first?")
        n = input()
        n = n.lower()
        if n == "history":
          Cprint("You enter the history section!")
          time.sleep(0.5)
          Cprint("You find an area which contains books on the history of the lake. You find the words 'Skyloft' written on one of the books.")
          time.sleep(1)
          Cprint("Do you wish to look at that book?")
          o = input()
          o = o.lower()
          if o == "yes":
            Cprint("You open the book.")
            time.sleep(0.25)
            Cprint("In the book you find a section on what is left behind in the lake. You see a map of where to find the stone.")
            time.sleep(2)
            Cprint("The pages warn of what danger you will have to overcome to get there, and the challenges that stand in your way.")
            time.sleep(2)
            Cprint("It says that the stone is guarded by the only fresh water sharks in the world. They are no ordinary sharks, and are extra dangerous.")
            time.sleep(2)
            Cprint("Once in the chamber of the stone, you must fight the undead water sorcerer, who survives on dark magic to this day.")
            time.sleep(2)
            Cprint("Of course to do this you will need weapons, so here is your inventory:")
            print(inventory)
            time.sleep(2)
            Cprint("In the future you can view your inventory when you get new items, need items, or before a fight")
            time.sleep(1)
            Cprint("Hmmmm. It seems your weapons are not good enough to fight through the obstacles you need to fight through.")
            time.sleep(2)
            Cprint("Let's go to the weapons shop to get some new equipment. Better bring that book with you too.")
            time.sleep(2)
            Cprint("You reach the weapons shop.")
            time.sleep(2)
            Cprint("The manager asks you what you are look for.")
            Cprint("Which would you like to say? a 'I am looking for a new sword' or b 'I am looking for a new bow'")
            p = input()
            p = p.lower()
            if p == "a":
              Cprint("They manager says 'ah, I have just the sword you need'")
              time.sleep(1)
              Cprint("He shows you two swords. One normal sword and one special enchanted sword.")
              time.sleep(1)
              Cprint("He says the normal one is 10 gold and the fancy one is 25 gold.")
              time.sleep(1.5)
              Cprint("Let's see if you have any gold in your inventory.")
              inventory.append("Gold: 75")
              time.sleep(1)
              Cprint("Here's your inventory: ")
              print(inventory)
              time.sleep(1.5)
              Cprint("It looks like you have some gold!")
              time.sleep(1)
              Cprint("Would you like to spend it?")
              q = input()
              q = q.lower()
              if q == "yes":
                  Cprint("Which one would you like to buy? a: normal sword or b: fancy sword?")
                  r = input()
                  r = r.lower()
                  if r == "a":
                      Cprint("You buy a normal sword!")
                      inventory.append("Normal Sword.")
                      time.sleep(0.5)
                      Cprint("Here's your inventory: ")
                      print(inventory)
                      Cprint("It is time for you to start your journey!")
                  elif r == "b":
                      Cprint("You buy a fancy sword!")
                      inventory.append("Fancy Sword.")
                      time.sleep(0.5)
                      Cprint("Here's your inventory: ")
                      print(inventory)
                      Cprint("It is time for you to start your journey!")
            elif p == "b":
              Cprint("The manager says: 'We have bows right over here.'")
              time.sleep(1)
              Cprint("We have a normal bow that comes with arrows, and a more powerful bow that comes with them too.")
              time.sleep(1.5)
              Cprint("Would you like a: the normal bow, or b: the powerful bow?")
              s = input()
              s = s.lower()
              if s == "a":
                  Cprint("You get the normal bow!")
                  inventory.append("Normal Bow.")
                  time.sleep(0.5)
                  Cprint("Here's your inventory: ")
                  print(inventory)
                  Cprint("It is time for you to start your journey!")
              elif s == "b":
                  Cprint("You get the powerful bow!")
                  inventory.append("Powerful bow!")
                  time.sleep(0.5)
                  Cprint("Here's your inventory: ")
                  print(inventory)
                  time.sleep(1)
                  Cprint("It is time for you to start your journey!")
          if o == "no":
            Cprint("You look elswhere.")
        elif n == "magic":
          Cprint("You enter the magic section!")
      elif i == "no" :
        Cprint("Do you wish to go to the docks where rumors of the fabled stone are passed?")
        j = input()
        j = j.lower()
        if j == "yes":
          Cprint("You go to the docks!")
        elif j == "no":
          Cprint("Restart the game.")
          gameplay = False
