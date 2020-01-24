import os
from room import Room
from player import Player

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from \
        west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

possible_inputs = "\nMovements:\n\n [n] = Northy\n [e] = East \n [s] = South \
    \n [w] = West\n\n\nGame Commands:\n\n [q] = quit"

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

player = Player(room['outside'])
user_input = None

# Clear the terminal
os.system('cls' if os.name == 'nt' else 'clear')

# Print the title
print("\n\n  Welcome to \n    THE GAME")

# Begin REPL loop
while user_input != "q":

    # if this is not the first loop, determined by the user_input clear the console
    if(user_input != None):
        os.system('cls' if os.name == 'nt' else 'clear')

    # Begin with printing the room
    print(player.room)

    # Prompt the player for user for input
    user_input = input(f"\nWhat direction would you like to go? \n ->")

    if(user_input.lower() == 'n'):
        if(player.room.n_to != None):
            player.room = player.room.n_to
        else:
            print(f'{player.room.get_name()} does not have a pasage to  the \
                North')
    elif(user_input.lower() == 'e'):
        if(player.room.e_to != None):
            player.room = player.room.e_to
        else:
            print(f'{player.room.get_name()} does not have a pasage to the \
                East')
    elif(user_input.lower() == 's'):
        if(player.room.s_to != None):
            player.room = player.room.s_to
        else:
            print(f'{player.room.get_name()} does not have a pasage to the \
                South')
    elif(user_input.lower() == 'w'):
        if(player.room.w_to != None):
            player.room = player.room.w_to
        else:
            print(f'{player.room.get_name()} does not have a pasage to the \
                West')
    elif(user_input.lower() == 'help'):
        print(possible_inputs)
    elif(user_input.lower() != 'q'):
        print('\nPlease enter a comand\nor type help for more information')

    print("\n")  # Alwase end the loop with a new line
