    #Characters
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
print("a")