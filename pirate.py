#choose character
def chooseCharacter():
    choice = input("Choose your character: Pirate or Merchant  ")

chooseCharacter()


#user input for name
ui = input("What's your name? ")
name = ui
print("Hi I'm " + name)

#define all functions
def shining():
    print("Oh no the shining wasn't treasure it is a dangerous sea creature!!!")
    print("This sea creature is unbeatable. It will kill you.")

def cave():
    print("Oh my god!!! You have found the treasure!!!!!")
    print("Congratulations! You have won!")

def winfight():
    print("Yay you beat the bad pirates! Now you may take this ship and some money to continue to sail.")
    sail = input("Choose to continue to sail to the shining or change course to the cave.  ")
    if sail == "shining":
        shining()
    elif sail == "cave":
        cave()
    else:
        print("Incorrect input. Please try again")
        winfight()

def losefight():
    print("You have been defeated and captured. Now these priates will kill you.")

def fight():
    shoot = input("You win some you lose some. Choose a random number between 1 and 5.  ")
    if shoot == "1":
        print("Oh no you were overpowered by the other pirates!")
        losefight()
    elif shoot == "2":
        winfight()
    elif shoot == "3":
        print("Oh no you were overpowered by the other pirates!")
        losefight()
    elif shoot == "4":
        print("Oh no you were overpowered by the other pirates!")
        losefight()
    elif shoot == "5":
        print("Oh no you were overpowered by the other pirates!")
        losefight()
    else:
        print("Incorrect input. Please try again")
        fight()

def surrender():
    print("Oh no you have been captured. These priates will torture you and kill you.")

def pirateship():
    print("Oh no! The ship is under attack.")
    attack = input("Choose to fight or surrender.  ")
    if attack == "fight":
        print("Argh I never surrender!")
        fight()
    elif attack == "surrender":
        print("I'm not a fighter.")
        surrender()
    else:
        print("Incorrect input. Please try again")
        pirateship()

def dingy():
    print("Yay you have avoided all the fighting on the pirate ship. Here is some money so you can continue to sail.")
    print("Hey look! What is that shining in the water up there? But there is also that very mysterious cave over there.")
    sail = input("Choose to continue to sail to the shining or change course to the cave.  ")
    if sail == "shining":
        shining()
    elif sail == "cave":
        cave()
    else:
        print("Incorrect input. Please try again")
        dingy()


def chooseShip():
    ship = input("Choose the big pirate ship or the small dingy.  ")
    if ship == "pirate ship":
        pirateship()
    elif ship == "dingy":
        dingy()
    else:
        print("Incorrect input. Please try again")
        chooseShip()

chooseShip()
