#Michelle Vo
#DH150 Final
#Winter 2018

import sys

#Global Variables#

commands = {'look': 'L',
            'north': 'N',
            'south': 'S',
            'east': 'E',
            'west': 'W',
            'pick up key': 'K',
            'open door': 'OD',
            'open chest': 'OC',
            'pick up sword': 'sword',
            'inventory': 'I',
            'attack monster': 'attack',
            'help': 'H'
            
            }

room = 0

isKeyInRoom = True
isSwordInRoom = False
doorIsLocked = True
chestOpened = False
doorIsLocked = True
keyInInventory = False
swordInInventory = False
MonsterIsAlive = True
PlayerIsAlive = True

stopBanging = 'Stop banging your head against a wall! \n'


def Help():
    print(str(list(commands.keys())) + '\n')

def Attack():
    global swordInInventory
    global MonsterIsAlive
    global PlayerIsAlive
    global room

    if (room != 3):
        print('You swung your fist into the air at nothing.')
    else:
        if (swordInInventory):
            print('You swung you sword and cut Grue\'s head off! \n')
            MonsterIsAlive = False
        else:
            print('Without a weapon in hand, you swung your fist at Grue. \n Grue bit off your arm and you ultimately died. \n')
            PlayerIsAlive = False

def Inventory():
    
    if (keyInInventory == False and swordInInventory == False):
        print('You have nothing in your inventory. \n')
        return

    print('You have: \n')
    if (keyInInventory == True):
        print('- a key \n')

    if (swordInInventory == True):
        print('- a mighty sword \n')        



# Looks at room and returns items and monsters.
def Look():
    global room
    if (room == 0):
        print('There is nothing here. \n')
        print('Exits: East or South. \n')
    if (room == 1):
        if (isKeyInRoom == True):
            print('There is a key in the room. \n')
        else:
            print('There is nothing here. \n')
            
        print('Exits: West or South. \n')

    if (room == 2):
        print('There is nothing here, though there is a door in the southern room. Grue, the monster, is to the east! \n')
        print('Exits: North, East, or South')
    if (room == 3):
        print('There is a monster here! \n')
        print('Exits: North or West')
    if (room == 4):
        if (chestOpened == False):
            print('There is a treasure chest! \n')
        else:
            if (isSwordInRoom == True):
                print('There is a sword in this room! You might need it, so pick it up!')
            else:
                print('There is only an empty treasure chest. \n')
        print('Exits: North')
        
def CheckLegalMove(direction):
    global room
    if (room == 0):
        if (direction == 'N' or direction == 'W'):
            print(stopBanging)
        else:
            MovePlayer(direction)
    elif (room == 1):
        if (direction == 'N' or direction == 'E'):
            print(stopBanging)
        else:
            MovePlayer(direction)
    elif (room == 2):
        if (direction == 'W'):
            print(stopBanging)
        else:
            MovePlayer(direction)
    elif (room == 3):
        if (direction == 'S' or direction == 'E'):
            print(stopBanging)
        else:
            MovePlayer(direction)
    elif (room == 4):
        if (direction != 'N'):
            print(stopBanging)
        else:
            MovePlayer(direction)

        

def MovePlayer(direction):
    global room
    if (direction == 'N'):
        print('Moving North!')
        if (room == 2):
            room = 0
        elif (room == 3):
            room = 1
        elif (room == 4):
            room = 2
    elif (direction == 'S'):
        print('Moving South!')
        if (room == 0):
            room = 2
        elif (room == 1):
            room = 3
        elif (room == 2):
            if (doorIsLocked == True):
                print('The door is locked! If only we had a key..')
            else:
                room = 4
    elif (direction == 'W'):
        print('Moving West')
        if (room == 1):
            room = 0
        elif (room == 3):
            room = 2
    elif (direction == 'E'):
        print('Moving East!')
        if (room == 0):
            room = 1
        elif (room == 2):
            room = 3


# Plays the game # 
def Game():
    global room
    global PlayerIsAlive 
    global MonsterIsAlive
    room = 0

    print('Welcome to Zork! This is a text-adventure game. See if you can defeat Grue!') 
    while (PlayerIsAlive and MonsterIsAlive):
        TakeAction()

    if (MonsterIsAlive == False and PlayerIsAlive == True):
        print('You Win! \n')
    elif (PlayerIsAlive == False and MonsterIsAlive == True):
        print('You Lost! \n')

    PlayerIsAlive = True
    MonsterIsAlive = True
    
    response = input('Wanna Play Again? \n')
    if (response == 'yes' or response == 'Yes'):
        Game()
    elif (response == 'no' or response == 'No'):
        sys.exit()
    else:
        print('Unknown input, so we\'ll just play again! \n')
        Game()
    

    

    

def ComputeAction(action):
    global room
    global isKeyInRoom
    global keyInInventory
    global doorIsLocked
    global isSwordInRoom
    global chestOpened
    global swordInInventory

    if (action == 'H'):
        Help()
    elif (action == 'L'):
        Look()
    elif (action == 'N' or action == 'S' or action == 'W' or action == 'E'): 
        CheckLegalMove(action)
    elif (action == 'K'):
        if (room != 1):
            print('What key are you talking about? \n')
        else:
            if (isKeyInRoom == True):
                isKeyInRoom = False
                print('You picked up a key! Maybe it will open a door... \n')
                keyInInventory = True
    
    elif (action == 'OD'):
         if (room != 2):
             print('What door are you talking about?')
         else:
             if (doorIsLocked == True):
                 if (keyInInventory == True):
                     print('You unlocked the door! Go south!')
                     doorIsLocked = False
                 else:
                     print('How can you unlock the door without a key?')
             else:
                  print('You already unlocked this door!')
                  
    elif (action == 'OC'):
         if (room != 4):
             print('What chest are you talking about?')
         else:
             if (chestOpened == False):
                 chestOpened = True
                 isSwordInRoom = True
                 print('You unlocked the chest and behold! A mighty sword! \n Why not try and pick up the sword?')              
             else:
                 print('You already opened the chest!')
    elif (action == 'sword'):
        if (room != 4 or isSwordInRoom == False):
            print('What sword are you talking about?')
        else:
            print('You picked up the sword!')
            swordInInventory = True
            isSwordInRoom = False
    elif (action == 'I'):
        Inventory()
    elif (action == 'attack'):
        Attack()
        
            
                
                
            
            
                     
                 
        
        
    


# Asks for Input #
def TakeAction():
    command = input('Type \'help\' to view commands. \nType a command: \n')
    if command not in commands:
        print('Invalid input. Try again \n')
    else:
        ComputeAction(commands[command])



#Activates Game!
Game()
