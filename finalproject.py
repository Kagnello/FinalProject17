# Definitions of Functions
    # Here I created functions for each room and direction choice so that the code ran smoothly and parts of the house/rooms could be revisited easily

    # First Choice of Direction
        # Choice allows user to choose a direction to go and then performs the function of that direction
def direction1():
    d1 = input("Which way do you want to go? Down the RIGHT HALLWAY, the LEFT HALLWAY, or UP THE STAIRS? \n").title()
    if d1== "Right Hallway":
        righthallway()
    elif d1== "Left Hallway":
        lefthallway()
    elif d1== "Up The Stairs":
        stairs()
    else:
        d1 = input("Which way do you want to go? Down the RIGHT HALLWAY, the LEFT HALLWAY, or UP THE STAIRS? \n").title()

    # Right Hallway
        # Tells user of their choice, continues the description of the story/house, and runs the function for the room cooresponding with this direction
def righthallway():
    print("You have chosen the right hallway. As the party walks, the floors creak. \nErin spots a door with a brass doorknocker (which seems a little strange since you're inside...)")
    room1()

    # Left Hallway
        # Tells user of their choice, continues the description of the story/house, and runs the function for the room cooresponding with this direction
def lefthallway():
    print("You have chosen the left hallway. The party walks down the hallway. It seems to get narrower and narrower until you reach a small door, no more than 3 feet tall. A sign says 'Please Knock'.")
    room2()

    # Up the Stairs
        # Tells user of their choice, continues the description of the story/house, and runs the function for the room cooresponding with this direction
def stairs():
    print("You have chosen to go up the stairs. Erin leads as the party walks up the stairs. As she steps on the 5th step, the stairs invert and turn into a slide. Everyone slides down into a dark room and fall on the floor.")
    room3()

    # Room 1
        # Asks the user if they wish to knock and describes or moves the characters accordingly
def room1():
    r1 = input("Do you knock? Y/N \n").upper()
    if r1== "Y":
        print(f"{character} knocks and the door opens by itself.")
        challenge1()
    if r1== "N":
        print("You continue to walk down the hallway to see that you've returned to the entryway.")
        direction1()

    # Room 2
        # Asks the user if they wish to knock and describes or moves the characters accordingly
def room2():
    r2 = input("Do you knock? Y/N \n").upper()
    if r2== "Y":
        print(f"{character} knocks and a small voice calls out, 'Come in!' ")
        challenge2()
    if r2== "N":
        print("You continue to walk down the hallway to see that you've returned to the entryway.")
        direction1()

    # Room 3
        # Asks the user if they wish to knock and describes or moves the characters accordingly
def room3():
    r3 = input("Do you FEEL FOR A LIGHTSWITCH or CHECK TO SEE IF EVERYONE IS OK ? \n").upper()
    if r3== "FEEL FOR A LIGHTSWITCH":
        print(f"Everyone is okay. {character} feels for a lightswitch. You discover one on the left wall and flick to reveal that you are in a jail cell.")
        challenge3()
    if r3== "CHECK TO SEE IF EVERYONE IS OK":
        print(f"{character} checks to see if everyone is okay and they all reply yes. You look around and find a lightswitch on the left wall. {character} flicks the lights on and the party discovers that they are in a jailcell.")
        challenge3()

    # Challenge Room 1
        # Describes the situation to the user. Prompts them with solutions to choose from. If a certain character is picked, then other options might be availiable to them
def challenge1():
    print("The party walks into the room. There is only a table with a crystal ball on it. \n It begins to glow and voice says: 'Bring me the thing with hands, but no arms, and a face, but no eyes. Then you may proceed.' \n")
    if character!= "Tyler":
        r1c1 = input("Do you ASK TYLER FOR HIS WATCH? Or TRY TO LEAVE anyway?\n").upper()
    if character== "Tyler":
        r1c2 = input("Do you PLACE YOUR WATCH on the table? Or TRY TO LEAVE anyway?\n").upper()

    # Challenge Room 2
        # Describes the situation to the user. Prompts them with solutions to choose from. If a certain character is picked, then other options might be availiable to them
def challenge2():
    print(f"The group walks into the room and sees a woman standing, looking at the wall. \n {character} asks, 'Are you ok?'. The woman replies, 'Yessss'. \n The woman's hair begins to move and {character} yells not to look.")
    if character!= "Caitlin":
        r2c1 = input("Do you ASK CAITLIN FOR HER MIRROR, COWER AND HOPE SHE GOES AWAY, or CLOSE YOUR EYES AND BLINDLY RUN PAST?\n")
    if character== "Caitlin":
        r2c2 = input("Do you USE YOUR MIRROR, COWER AND HOPE SHE GOES AWAY, or CLOSE YOUR EYES AND BLINDLY RUN PAST?\n")

    # Challenge Room 3
        # Describes the situation to the user. Prompts them with solutions to choose from. If a certain character is picked, then other options might be availiable to them
def challenge3():
    print(f"You see that across the way from your cell is another, open, with an animal inside. {character} calls out for help. The animal turns and reaches out his hand.")
    if character!= "Matt":
        r3c1 = input("Do you ASK MATT FOR HIS GRANOLA BAR, GIVE HIM A HIGH 5, or TRY TO FIND YOUR OWN WAY OUT?\n")
    if character== "Matt":
        r3c2 = input("Do you OFFER YOUR GRANOLA BAR, GIVE HIM A HIGH 5, or TRY TO FIND YOUR OWN WAY OUT?\n")


#CHARACTERS
    #Created a Class of Characters and inputted names, healths, inventories, strengths, and weaknesses for each character
class Characters(object):
    def __init__(self, health, inventory, strengths, weaknesses):
        self.health = 100
        self.inventory = inventory
        self.strengths = strengths
        self.weaknesses = weaknesses
Caitlin = Characters(100, "Mirror", "Observant", "Reckless")
Tyler = Characters(100, "Watch", "Leader", "Stubborn")
Erin = Characters (100, "Notebook", "Intelligent", "Perfectionist")
Matt = Characters(100, "Granola Bar", "Strong", "Uncooperative")

charlist = ["Caitlin", "Tyler", "Erin", "Matt"]

# INTRO
    # Prints a welcome message and asks for the user to pick between characters through an input and prints a statement based on which character they chose
        # Allows the user to start and learn about the game
print("Welcome! You and your friends are walking in the forest when you stumble upon an abandoned house. You decide to check it out. Before you enter...")
character = input("Which character do you choose? \n Caitlin (Inventory Item: Mirror) (Strength: Observant) (Weakness: Reckless) \n Tyler (Inventory Item: Watch) (Strength: Leader) (Weakness: Stubborn) \n Erin (Inventory Item: Notebook) (Strength: Intelligent) (Weakness: Perfectionist) \n Matt (Inventory Item: Granola Bar) (Strength: Strong) (Weakness: Uncooperative) \n").title()
while True:
    if character in charlist:
        print(f"Great! You are {character}. \n When choices arise, type your answer in accordance with the uppercase phrases. \n Your character and your party will travel through the abondaned house. \n Try to make it out alive! ")
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
direction1()

    # ROOMS 1-3

    # ROOM 1
while direction1== "Right Hallway":
    room1()
    break

    # ROOM 2
while direction1== "Left Hallway":
    room2()
    break

    # ROOM 3
while direction1== "Up The Stairs":
    room3()
    break


