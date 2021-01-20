import time
import random

opponent = 'none'

#Ogre Stats
ogreHitPoints = 59
ogreArmor = 11
ogreToHitModifier = 8
ogreDamageMax = 16
ogreDamageModifier = 4
ogreDamageType = 'Bludgeoning'
#Goblin Stats
goblinHitPoints = 7
goblinArmor = 15
goblinToHitModifier = 4
goblinDamageMax = 6
goblinDamageModifier = 2
goblinDamageType = 'Slashing'
#Zombie Stats
zombieHitPoints = 22
zombieArmor = 8
zombieToHitModifier = 3
zombieDamageMax = 6
zombieDamageModifier = 1
zombieDamageType = 'Bludgeoning'

def textPrint(text,t):

    Ltext=list(text)
    for i in range(0,len(Ltext)-1):
        print(Ltext[i],end='')
        time.sleep(t)
    print(Ltext[len(Ltext)-1])
    
def encounterOpponent(opponent):

    opponent.lower

    if opponent == 'ogre':
        
        print('(Debug) ogreHitPoints = ' + str(ogreHitPoints))
        print('(Debug) ogreArmor = ' + str(ogreArmor))
        print('(Debug) ogreToHitModifier = ' + str(ogreToHitModifier))
        print('(Debug) ogreDamageMax = ' + str(ogreDamageMax))
        print('(Debug) ogreDamageModifier = ' + str(ogreDamageModifier))
        print('(Debug) ogreDamageType = ' + str(ogreDamageType))
        
    if opponent == 'goblin':
        
        print('(Debug) goblinHitPoints = ' + str(goblinHitPoints))
        print('(Debug) goblinArmor = ' + str(goblinArmor))
        print('(Debug) goblinToHitModifier = ' + str(goblinToHitModifier))
        print('(Debug) goblinDamageMax = ' + str(goblinDamageMax))
        print('(Debug) goblinDamageModifier = ' + str(goblinDamageModifier))
        print('(Debug) goblinDamageType = ' + str(goblinDamageType))

    if opponent == 'zombie':

        print('(Debug) zombieHitPoints = ' + str(zombieHitPoints))
        print('(Debug) zombieArmor = ' + str(zombieArmor))
        print('(Debug) zombieToHitModifier = ' + str(zombieToHitModifier))
        print('(Debug) zombieDamageMax = ' + str(zombieDamageMax))
        print('(Debug) zombieModifier = ' + str(zombieDamageModifier))
        print('(Debug) zombieDamageType = ' + str(zombieDamageType))

    print('You have encountered an ' + opponent + ', get ready to fight!')

print('Welcome to Five Coffee Cups!')
time.sleep(1)
print('In this text based adventure game you will explore and fight monsters along the way.')
time.sleep(1)
print('The game will now begin!')
time.sleep(1)
a = 1
for a in ('this text is used as a spacer to space out the previous text from the actual game enviroment'):
    print('')
    time.sleep(0.01)

b = 1
for b in ('repeat this loop for a really long time yeah so um im just gonna use this to write my robotics notebook entries now.'):
    print('Where do you want to start you adventure?')
    print('You can either start at the wizard tower, the town of (to be named), or the dwarven mines')
    starterLocation = input()
    starterLocation.lower
    if starterLocation == 'wizard tower' or starterLocation == 'the town of (to be named)' or starterLocation == 'the dwarven mines':
        print('You have chosen to start at the ' + starterLocation + ', is this correct?')
        yesQuestion = input()
        yesQuestion.lower
        if yesQuestion == 'yes':
            print('loading...')
            a = 1
            for a in ('this text is used as a spacer to space out the previous text from the actual game enviroment'):
                print('')
                time.sleep(0.01)
    else:
        raise Exception('Invalid input please restart the program')
    
    if starterLocation == 'wizard tower':
        print('You wake up laying down in a large circular room')
        print('what do you want to do?')
        print('you can sit up, or look around while laying down')
        print('type \'sit up\' or \'look around\'')
        choice = input()
        choice.lower
        if choice == 'sit up' or choice == 'look around':
            if choice == 'sit up':
                print('you sit up and look around and see many vials and glasses of random liquids you don\'t recogize')
                print('What do you want to do?')
                print('You can stand up and walk around, or stay sitting')
                print('Type \'stand up\' or \'stay sitting\'')
                choice = input()
                choice.lower
                if choice == 'stand up':
                    print('You stand up and start walking around the room looking at the vials of different colors')
                    print('What do you want to do?')
                    print('You can walk around, or inspect the vials closer')
                    print('Type \'walk around\' or \'inspect vials\'')
                    choice = input()
                    if choice == 'walk around':
                        print('You continue to walk around and look at the vials when someone walks into the room from the spiral staircase on the far side of the room)
                    if choice == 'inspect vials':
                        print('You are inspecting the vials when a person walks into the room from a spiral staircase situated on the far side of the room')
                    
                if choice == 'stay sitting':
                    print('You stay sitting down and look down the rows of multicolored vials.')
                    print('What do you want to do?')
                    
            if choice == 'look around':
                print('you look around but from your limited view from the bed you can\'t really see anything')

    if starterLocation == 'the town of (to be named)':
        print('You wake up laying down in a small square room')

    if starterLocation == 'the dwarven mines':
        print('You wake up laying down on a cot in a large cave')
                              
print('e')

    break
