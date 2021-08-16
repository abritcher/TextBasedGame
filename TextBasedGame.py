
# Alexander Britcher

import random
import os


# How to play instructions
def how_to_play():
    print()
    print()
    print()
    print("               |||||||||||||||||||       |||        |||        |||||||||||||\n"
          "                       |||               |||        |||        |||\n"
          "                       |||               |||        |||        |||\n"
          "                       |||               ||||||||||||||        ||||||||\n"
          "                       |||               |||        |||        |||\n"
          "                       |||               |||        |||        |||\n"
          "                       |||               |||        |||        |||||||||||||")
    print("||||||||\n"
          "  ||||            ||        |||||||   ||      ||  |||||||    ||||||||  |||     ||  ||||||||||  ||       ||\n"
          "  ||||           ||||       ||    ||   ||    ||   ||    ||      ||     ||||    ||      ||      ||       ||\n"
          "  ||||          ||  ||      ||    ||    ||  ||    ||    ||      ||     || ||   ||      ||      ||       ||\n"
          "  ||||         ||    ||     ||||||       ||||     ||||||        ||     ||  ||  ||      ||      |||||||||||\n"
          "  ||||        ||||||||||    ||    ||      ||      ||   ||       ||     ||   || ||      ||      ||       ||\n"
          "  ||||       ||        ||   ||    ||      ||      ||    ||      ||     ||    ||||      ||      ||       ||\n"
          "  ||||      ||          ||  |||||||       ||      ||     ||  ||||||||  ||     |||      ||      ||       ||\n"
          "  ||||\n"
          "|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n")
    print()
    print()
    print()
    print("A text-based adventure game designed to challenge you\n")
    print("Press enter to start")
    input()
    os.system('cls')
    print("How to play:\n"
          "You have the ability to go north, south, east, or west depending on the room you are in.\n"
          "You do this by typing \"Go [Direction]\"\n"
          "You can also get any item in the room by typing \"Get [name of item]\"\n"
          "The goal of the game is to collect all 6 items before encountering the monster.\n"
          "Be careful; the monster, items, and room you start in change every game.\n"
          "Good Luck!\n")
    print("Press enter to start your adventure!")
    input()
    os.system('cls')


# Intro
def intro():
    print("You wake cold, naked, and feeling injured in a dimly lit room.\n"
          "You have no idea how you got here or what happen to you.\n"
          "Off in the distance you hear something big and dangerous.\n"
          "You definitely don't want to encounter whatever that is in your current condition.\n"
          "Maybe you can find some items to help you deal with the source of that terrible sound...\n")


# Movement function
def movement():
    global current_room
    global valid_choice
    global choice
    if choice[-1] not in directions_dict.keys():
        os.system('cls')
        print("I'm sorry, that is not a direction.")
        print("Try entering north, east, south, or west")
        print()
    else:
        new_room = current_room + directions_dict[choice[-1]]
        if new_room < 1 or new_room > 9:
            os.system('cls')
            print(no_door)
        elif current_room * new_room == 12 or current_room * new_room == 42:
            os.system('cls')
            print(no_door)
        else:
            os.system('cls')
            current_room = new_room
        valid_choice = 'yes'


# Get item function
def get_item():
    global inventory
    global item_room_dict
    global choice
    if current_room in item_room_dict and choice[-1] == item_description[item_room_dict[current_room]][0]:
        inventory.append(item_description[item_room_dict[current_room]][2])
        os.system('cls')
        print(item_description[item_room_dict.pop(current_room)][1])
    else:
        os.system('cls')
        print("There is no", choice[-1], "in the room.")


directions_dict = {'north': 3, 'east': 1, 'south': -3, 'west': -1}
item_description = {'item1': ['sword', "You got a sword! Now you have the power to kill things!", 'Sword'],
                    'item2': ['shield', "You got a shield! You can now block attacks!", 'Shield'],
                    'item3': ['helmet', "You got a helmet! Your head is now nice and protected!", 'Helmet'],
                    'item4': ['set of armour', "You got a set of armour! You body is much more protected!", 'Armour'],
                    'item5': ['health potion', "You got a health potion! Drinking it makes you feel much better!",
                              'Health Potion'],
                    'item6': ['set of clothing', "You found a set of clothing! Now you're not naked!", 'Clothing']}
room_description = {1: "You see a doorway to your north and east",
                    2: "You see a doorway to your west, north, and east",
                    3: "You see a doorway to your west and north",
                    4: "You see a doorway to your north, east, and south",
                    5: "You see a doorway to your north, east, south, and west",
                    6: "You see a doorway to your west, north, and south",
                    7: "You see a doorway to your east and south",
                    8: "You see a doorway to your west, east, and south",
                    9: "You see a doorway to your west and south"}
no_door = "There is no doorway in that direction\n"
item_room_dict = {}
inventory = []
choice = []
current_room = []
valid_choice = []


def main():
    global inventory
    global choice
    global current_room
    global valid_choice
    play_again = 'y'

    while play_again == 'y':
        villain_encountered = 'no'
        avl_rooms = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        inventory = []
        item_room_dict.clear()
        os.system('cls')

# Assign random rooms for spawn, villain, and items
        current_room = avl_rooms.pop(random.randint(0, 8))
        villain_room = avl_rooms.pop(random.randint(0, 7))
        for i in range(1, 7):
            item_room = avl_rooms.pop(random.randint(0, (7-i)))
            item_room_dict[item_room] = ('item' + str(i))

# How to play and intro
        how_to_play()
        intro()

# Gameplay loop
        while villain_encountered == 'no':
            valid_choice = 'no'

            while valid_choice == 'no':
                print(room_description[current_room])
                print()
                if current_room in item_room_dict:
                    print("You see a", item_description[item_room_dict[current_room]][0])
                    print()
                print('Inventory:', inventory)
                print()
                print("What would you like to do?")
                print()

                user_choice = input()
                choice = user_choice.lower().split(' ', 1)

# No input
                if user_choice == '':
                    os.system('cls')
                    break

# Movement
                elif choice[0] == 'go':
                    movement()

# Get item
                elif choice[0] == 'get':
                    get_item()

# Invalid input
                else:
                    os.system('cls')
                    print("Try entering a valid command (go ......, get .......)")
                    print()

# Check if in villain room
            if current_room == villain_room:
                villain_encountered = 'yes'

# Battle villain
        os.system('cls')
        print("As you enter the room a powerful stench overtakes you.\n"
              "You see dead bodies strewn around the room and in the middle of the room you see a massive minotaur.")
        print("It lets out a mighty roar and charges right at you!")
        print("Now is the time you must fight for your life!\n")
        print("Press enter to fight!")
        input()
        os.system('cls')


# Lose battle with item-specific statements
        if len(inventory) != 6:
            if 'Sword' not in inventory:
                print("You realize you have nothing to attack the minotaur with!\n"
                      "You dodge some blows but with no way to fight back you end up taking to much damage and die.\n")
            elif 'Shield' not in inventory:
                print("You strike out with your sword landing a nice blow on the minotaur.\n"
                      "\"I just might be able to win this\" you think to yourself\n"
                      "Your confidence is short lived as the minotaur takes a swing at you "
                      "and you have no way to block it!")
                if 'Armour' in inventory:
                    print("Your suit of armour reduces the impact from some of the blows but they just keep coming!\n")
                else:
                    print("With no real way to defend yourself you eventually succumb to the damage and die.\n")
            elif 'Armour' not in inventory:
                print("You quickly block the minotaur's blow with your shield and counter attack with your sword.\n"
                      "\"I just might be able to win this\" you think to yourself\n"
                      "Your confidence is short-lived as the minotaur howls and delivers a swift series of blows\n"
                      "You manage to block a few but there are just too many.\n"
                      "Eventually one gets past your shield and hits you right in the chest.\n"
                      "Way too much damage. As your vision closes in to a single point you \n"
                      "find yourself wishing that you had more protection for your body.\n")
            elif 'Helmet' not in inventory:
                print("You quickly block the minotaur's blow with your shield and counter attack with your sword.\n"
                      "\"I just might be able to win this\" you think to yourself\n"
                      "You trade blows with the minotaur, successfully blocking most with your shield.\n"
                      "Those that you don't block barely hurt you due to your armour\n"
                      "You smile, feeling like your victory has been assured\n"
                      "That's when you get hit right in the face, shattering your smiling teeth.\n"
                      "Your vision blurs and in your weakened state the minotaur finished you off.\n"
                      "You should have protected your head.\n")
            elif 'Clothing' not in inventory:
                print("You quickly block the minotaur's blow with your shield and counter attack with your sword.\n"
                      "\"I just might be able to win this\" you think to yourself\n"
                      "You trade blows with the minotaur, successfully blocking most with your shield.\n"
                      "Those that you don't block barely hurt you due to your armour\n"
                      "As the battle goes on you notice that your armour is sticking to your bare skin \n"
                      "and restricting your movement.\n"
                      "You slow down more and more and even begin to chafe.\n"
                      "While thinking about the annoying blisters that you will inevitably develop the minotaur "
                      "catches you off-guard and kills you.\n"
                      "You should have stayed focused.\n")
            elif 'Health Potion' not in inventory:
                print("You quickly block the minotaur's blow with your shield and counter attack with your sword.\n"
                      "\"I just might be able to win this\" you think to yourself\n"
                      "You trade blows with the minotaur, successfully blocking most with your shield."
                      "Those that you don't block barely hurt you due to your armour\n"
                      "Unfortunately your weren't too healthy to begin with.\n"
                      "After a couple more blows you collapse, unable to stand.\n"
                      "As the minotaur walks over to finish you off you find yourself more angry than anything.\n"
                      "You totally could have won the fight if you didn't start it already injured.\m")
            print("You Lose!")
        else:
            print("You quickly block the minotaur's blow with your shield and counter attack with your sword.\n"
                  "\"I just might be able to win this\" you think to yourself\n"
                  "You trade blows with the minotaur, successfully blocking most with your shield."
                  "Those that you don't block barely hurt you due to your armour\n"
                  "Eventually you manage to overcome the minotaur and deal a clean blow, striking its head clear off!\n"
                  "You collapse on the ground, alive but exhausted.\n")
            print("you survived\n")
            print()
            print("Congratulations! You have defeated the minotaur and beaten The Labyrinth!")

# Play again?
        print("Would you like to play again?")
        print('y/n')
        play_again = input()


if __name__ == "__main__":
    main()

print("Thanks for playing!")
