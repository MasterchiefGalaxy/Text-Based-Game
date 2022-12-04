import time


def introduction():
    print()


print('***********The Realm of Slumber***********')
print('You are asleep in a deep dream. As your eyes open \n you notice you are in a dark place'
      ' a cave perhaps....... \n'
      'You hear the sounds of a monster in the distance, taunting you. \n Can you navigate the corridors \n'
      'of the cave to find the hidden items needed to defeat the MONSTER and escape this dream??')
print('***************************************************************************************************')
print('You must collect all six items to defeat the monster!!!')
print('***** move commands: north, east, south, west *****')
print('***** add item to inventory: Y/N *****')
print('To exit type: Exit')
time.sleep(1.0)

rooms = {
    'entrance': {'east': 'kitchen', 'west': 'entrance', 'south': 'hallway'},
    'kitchen': {'item': 'sword', 'west': 'entrance'},
    'hallway': {'item': 'helmet', 'west': 'west wing', 'east': 'east wing', 'south': 'south wing'},
    'west wing': {'item': 'lantern', 'east': 'hallway'},
    'east wing': {'item': 'armor', 'north': 'library', 'west': 'hallway'},
    'library': {'item': 'shield', 'south': 'east wing'},
    'south wing': {'item': 'torch', 'north': 'hallway', 'east': 'monster room'},
    'monster room': {'item': 'SNARLING MONSTER'}

}
def player_status():
    print('***************************************************')
    print('\nYou are currently in the {}'.format(currentRoom))
    print('\nYour current inventory: {}'.format(inventory))
    print('\n***************************************************')
    print('\n')
inventory = []

user_item = ''


def game(item):
    if item in inventory:
        print("you already have this")
        print(" ".join(inventory))

    elif item not in inventory:
        print('You see the', item)
        print('Would you like to pick up the item? \n')
        user_item = input('')
        if user_item == 'Y':
            print('item has been added\n')
            inventory.append(item)
        else:
            print('You leave the item behind.')


currentRoom = 'entrance'

player_move = ''

introduction()

while True:
    player_status()

    player_move = input('Enter a move: \n')

    if player_move == 'Exit':
        print('Time to wake up!')
        break

    if player_move in rooms[currentRoom]:
        currentRoom = rooms[currentRoom][player_move]

        addItem = input(' \n')

        if 'item' in rooms[currentRoom]:
            game(rooms[currentRoom]['item'])

        if currentRoom == 'monster room':
            if len(inventory) == 7:
                print('\n***** YOU HAVE AWOKEN*****')
                time.sleep(1.0)
                print('\n************************************************************************')
                print('\nYou have made it out of the dream alive and in hopes to never return!!')
                print('*************************************************************************\n')
                time.sleep(1.0)
                print('***** THE END *****\n')
                break
