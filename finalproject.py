    #CHARACTERS
class Characters(object):
    def __init__(self, health, inventory, strengths, weaknesses):
        self.health = 100
        self.inventory = inventory
        self.strengths = strengths
        self.weaknesses = weaknesses
Caitlin = Characters(100, "Mirror", "Observant", "Reckless")
Tyler = Characters(100, "Baseball", "Leader", "Stubborn")
Erin = Characters (100, "Notebook", "Intelligent", "Perfectionist")
Matt = Characters(100, "Granola Bar", "Strong", "Uncooperative")

charlist = ["Caitlin", "Tyler", "Erin", "Matt"]

    # INTRO
print("Welcome! You and your friends are walking in the forest when you stumble upon an abandoned house. You decide to check it out. Before you enter...")
character = input("Which character do you choose? \n Caitlin (Inventory Item: Mirror) (Strength: Observant) (Weakness: Reckless) \n Tyler (Inventory Item: Baseball) (Strength: Leader) (Weakness: Stubborn) \n Erin (Inventory Item: Notebook) (Strength: Intelligent) (Weakness: Perfectionist) \n Matt (Inventory Item: Granola Bar) (Strength: Strong) (Weakness: Uncooperative) \n").title()
while True:
    if character in charlist:
        print(f"Great! You are {character}.")
        start = input("To begin, type 'Start'. \n").title()
        break
    else:
        character = input("That is not a character. Try again: ").title()

while True:
    if start=="Start":
        print(f"\n {character} knocks on the door. There is no answer. \n Matt pushes the door to find that it is open. The party steps inside the house. \n Before you is a dusty crystal chandelier, an entry table, and a grand staircase with hallways on either side.")
        break
    else:
        print(f"Great! You are {character}.")
        start = input("To begin, type 'Start'. \n").title()

    # FIRST CHOICE OF DIRECTION
direction1 = input("Which way do you want to go? Down the RIGHT HALLWAY, the LEFT HALLWAY, or UP THE STAIRS? \n").title()
while True:
    if direction1== "Right Hallway":
        print("You have chosen the right hallway. As the party walks, the floors creak. \nErin spots a door with a brass doorknocker (which seems a little strange since you're inside...)")
        room1 = input("Do you knock? Y/N \n").upper()
        break
    if direction1== "Left Hallway":
        print("You have chosen the left hallway. The party walks down the hallway. It seems to get narrower and narrower until you reach a small door, no more than 3 feet tall. A sign says 'Please Knock'.")
        room2 = input("Do you knock? Y/N \n").upper()
        break
    if direction1== "Up The Stairs":
        print("You have chosen to go up the stairs. Erin leads as the party walks up the stairs. As she steps on the 5th step, the stairs invert and turn into a slide. Everyone slides down into a dark room and fall on the floor.")
        room3 = input("Do you FEEL FOR A LIGHTSWITCH or CHECK TO SEE IF EVERYONE IS OK ? \n").upper()
        break

    # ROOMS 1-3

    # ROOM 1
while direction1 == "Right Hallway":
    if room1== "Y":
        print("{character} knocks and the door opens by itself.")
        break
    if room1== "N":
        print("You continue to walk down the hallway to see that you've returned to the entryway.")
        direction1 = input("Which way do you want to go? Down the RIGHT HALLWAY, the LEFT HALLWAY, or UP THE STAIRS? \n").title()

    else:
        print("That is not an answer.")
        room1 = input("Do you knock? Y/N \n").upper()

    # ROOM 2
while direction1== "Left Hallway":
    if room2== "Y":
        print("{character} knocks and a small voice calls out, 'Come in!' ")
        break
    if room2== "N":
        print("You continue to walk down the hallway to see that you've returned to the entryway.")
        direction1 = input("Which way do you want to go? Down the RIGHT HALLWAY, the LEFT HALLWAY, or UP THE STAIRS? \n").title()

    else:
        print("That is not an answer.")
        room2 = input("Do you knock? Y/N \n").upper()

    # ROOM 3
while direction1== "Up The Stairs":
    if room3== "Feel For A Lightswitch":
        print("Everyone is okay. {character} feels for a lightswitch. You discover one on the left wall and flick to reveal that you are in a jail cell.")
        break
    if room3== "Check To See If Everyone Is Ok":
        print("{character} checks to see if everyone is okay and they all reply yes. You look around and find a lightswitch on the left wall. {character} flicks the lights on and the party discovers that they are in a jailcell.")
        break
    else:
        print("That is not an answer.")
        room3 = input("Do you FEEL FOR A LIGHTSWITCH or CHECK TO SEE IF EVERYONE IS OK? \n").upper()
