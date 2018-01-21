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
        direction1()

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
    else:
        room2()

    # Room 3
        # Describes the situation and Asks the user to pick an option for the situation
def room3():
    r3 = input("Do you FEEL FOR A LIGHTSWITCH or CHECK TO SEE IF EVERYONE IS OK ? \n").upper()
    if r3== "FEEL FOR A LIGHTSWITCH":
        print(f"Everyone is okay. {character} feels for a lightswitch. You discover one on the left wall and flick to reveal that you are in a jail cell.")
        challenge3()
    if r3== "CHECK TO SEE IF EVERYONE IS OK":
        print(f"{character} checks to see if everyone is okay and they all reply yes. You look around and find a lightswitch on the left wall. {character} flicks the lights on and the party discovers that they are in a jailcell.")
        challenge3()
    else:
        room3()

# Room 4
        # Describes the situation and Asks the user to pick an option for the situation
def room4():
    print(f"The party walks down the dark hallway. {character} runs their hand along the left wall and suddenly feels a door knob. \n The party enters the room, looking for a way out.")
    r4 = input(f"In the room the group finds an empty room. After {character} walks through last, the door closes. \n Suddenly a bat swoops down on the party! Do you USE ERIN'S NOTEBOOK to hit it? Or RUN AROUND SCREAMING? \n").upper()
    if r4== "USE ERIN'S NOTEBOOK":
        print(f"{character} uses Erin's notebook and hits the bat. It falls to the ground. \n \n")
        print(f"The party realized that although they had defeated all the monsters, they didn't have a way out. \n {character} felt around the room while everyone else sat down, accepting defeat. \n Suddenly, {character} found a small keyhole in the wall. \n {character} yelled out, 'Does anyone know where a key would be?' \n The group search the room until Caitlin exclaimed, 'I found it!' \n {character} put the key into the keyhole and the wall opened to sunlight. \n The party ran out of the house. They ran to their homes and decided that they would never discuss the events that occurred in the house again. \n THE END.")
    if r4== "RUN AWAY SCREAMING":
        print(f"{character} and the rest of the group run around screaming. This only angers the bat more. It picks the group off one by one. \n GAME OVER")
        direction1()


# Room 5
        # Describes the situation and Asks the user to pick an option for the situation
def room5():
    r5 = input(f"The group goes through the door and finds yet another door not 2 feet away. {character} turns the knob and the party enters. Here they all enter to a dark room. \n The door closes and Matt feels the ground and concludes that they are standing on sand. \n Suddenly, the group starts sinking! \n Do you THRASH AROUND or KEEP STILL? \n").upper()
    if r5== "THRASH AROUND":
        print("The group all move around, trying to get out of the quicksand. \n This makes them sink faster. \n GAME OVER ")
        direction1()
    if r5== "KEEP STILL":
        print(f"{character} yells for everyone to keep still. They do and everyone travels through the quicksand to find themselves back in the entry way.")
        direction1()
    else:
        print("That is not an answer.")
        room5()

# Room 6
        # Describes the situation and Asks the user to pick an option for the situation
def room6():
    r6 = input("The group climbs the stairs and turns to enter the next room, as directed by the animal in the cells. They run into the room and stumble to a stop as they run into a pair of giant feet. \n 'WHO DARES DISTURB ME?!' The giant's voice boomed. Tyler yells to scatter. \n Do you GRAB THE ROPE off the wall, YELL BACK, or RUN AROUND? \n").upper()
    if r6== "GRAB THE ROPE":
        print(f"{character} grabs rope off the wall and throws it to someone across the room. {character} yells, 'Someone distract him and we'll trip him!' \n While the other two distracted the giant, the pair tied the rope around the giant's feet. \n He fell to the ground with a CRASH! \n The party celebrates and quickly moves to go through to the next room before the giant gets up again.")
        print("However, as the group passes through the doorway, they find themselves back in the entryway.")
        direction1()
    if r6== "YELL BACK":
        print(f"{character} yells back, 'We're sorry, but we're just trying to get out of here! Could you cut us some slack?' \n Surprisingly, the giant replies, 'Oh, I'm so sorry. I understand and I'll get out of your way. Good luck!' \n The group moved on happily thanking the giant.")
        print("The party finds themselves back in the entryway.")
        direction1()
    if r6== "RUN AROUND":
        print(f"The group runs around trying to get away from the giant. \n This doesn't work and the giant catches them all. \n GAME OVER")
        direction1()
    else:
        print("That is not an answer.")
        room5()

    # Challenge Room 1
        # Describes the situation to the user. Prompts them with solutions to choose from. If a certain character is picked, then other options might be availiable to them
def challenge1():
    print("The party walks into the room. There is only a table with a crystal ball on it. \n It begins to glow and voice says: 'Bring me the thing with hands, but no arms, and a face, but no eyes. Then you may proceed.' \n")
    r1c = input("Do you USE TYLER'S WATCH? Or TRY TO LEAVE anyway?\n").upper()
    if r1c== "USE TYLER'S WATCH":
        print(f"{character} places the watch on the table and the same voice rings out: 'That is correct.' \n A panel opens behind the table and the party begins to walk down the dark hallway now revealed.")
        room4()
    if r1c== "TRY TO LEAVE":
        print(f"{character} says, 'This is ridiculous.' Someone says, 'Maybe we should listen.' {character} decides not to and trys to go back through the door that the party came through. \n 'HOW DARE YOU!' The voice rang out. Suddenly, the door closes with a slam. The party was trapped. \n GAME OVER ")
        direction1()


    # Challenge Room 2
        # Describes the situation to the user. Prompts them with solutions to choose from. If a certain character is picked, then other options might be availiable to them
def challenge2():
    print(f"The group walks into the room and sees a woman standing, looking at the wall. \n {character} asks, 'Are you ok?'. The woman replies, 'Yessss'. \n The woman's hair begins to move and {character} yells not to look.")
    r2c = input("Do you USE CAITLIN'S MIRROR, COWER AND HOPE SHE GOES AWAY, or CLOSE YOUR EYES AND BLINDLY RUN PAST?\n").upper()
    if r2c== "USE CAITLIN'S MIRROR":
        print(f"{character} holds Caitlin's mirror up and the woman screeches. \n The party looks up to see that the woman has turned to stone and that there is a door behind her. The party walks through it and continues on.")
        room5()
    if r2c== "COWER AND HOPE SHE GOES AWAY":
        print("The party cowers and hopes she goes away. This doesn't work. One by one they look up and they all turn to stone. \n GAME OVER")
        direction1()
    if r2c== "CLOSE YOUR EYES AND RUN BLINDLY PAST":
        print(f"{character} closes their eyes and tries to run past. This doesn't work. {character} crashes into the woman, looks up, and becomes stone. \n GAME OVER")
        direction1()
    else:
        print("That is not an answer.")
        challenge2()

    # Challenge Room 3
        # Describes the situation to the user. Prompts them with solutions to choose from. If a certain character is picked, then other options might be availiable to them
def challenge3():
    print(f"You see that across the way from your cell is another, open, with an animal inside. {character} calls out for help. The animal turns and reaches out his hand.")
    r3c = input("Do you USE MATT'S GRANOLA BAR, GIVE HIM A HIGH 5, or TRY TO FIND YOUR OWN WAY OUT?\n").upper()
    if r3c== "USE MATT'S GRANOLA BAR":
        print(f"{character} uses Matt's granola bar and throws it at the animal. It turns, says thank you in surprisingly good English. \n He opens the cage and the party walks out. {character} says thank you. \n The animal tells them that the way out is to go upstairs and into the next room. The party continues. ")
        room6()
    if r3c== "GIVE HIM A HIGH 5":
        print(f"{character} gives the animal a high five. The animal growls at the disrespect and lunges at the party. \n GAME OVER")
        direction1()
    if r3c== "TRY TO FIND YOUR OWN WAY OUT":
        print(f"{character} says 'This is ridiculous! We'll find our own way out.' \n The party doesn't find their way out. \n GAME OVER")
        direction1()
    else:
        print("That is not an answer.")
        challenge3()


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

    # ROOMS
while direction1== "Right Hallway":
    room1()
    room4()
    break

while direction1== "Left Hallway":
    room2()
    room5()
    break

while direction1== "Up The Stairs":
    room3()
    room6()
    break


