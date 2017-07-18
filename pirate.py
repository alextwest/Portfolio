import time

import msvcrt as m
name = input("Oy mate! What do you call yourself?  ")
print("Welcome aboard, Captian " + name)

def wait():
    m.getch()

wait()

def pstoryline():
    print("Although the seas are infested with pirates and scoundrels, only one name striks the chord of fear in people so profoundly as Captain " + name)
    wait()
    print("You and your crew are roming the seven seas hunting for treasure")
    wait()
    print("Along your travles you have encountered storms and mythical beasts, death and catastrophe")
    wait()
    print("But you endevor through it all in hopes of finding the alleged 'Treasure of Amora'")

    #wait for five seconds
    wait()

    print("As you look out into the gray horizon, you see shadowy figures that can easily be recognized as fellow shipmongers")
    wait()
    print("you've been traveling at sea for many moons and both you and your crew is starving for food as well as excitement")
    wait()
    print("Your pirate sailors agree its time to have some fun!")

#wait for five seconds
    wait()

    print("Multiple ships prowl the water around you.")
    wait()
    print("out of all of them, two ships catch your eye")
    wait()
    print("A magnifacent ship with an ink black starboard, the mast so tall it disappears into the fog.")
    wait()
    print("The second ship is a small dingy, and you see only a few sailors aboard")
    wait()
    print("You are confident you will capture the dingy swiftly but you're not sure you it has much treasure aboard")
    wait()
    print("The other ship however, seems to have much treasure aboard but you dont know if you have enough manpower to overcome them")

    #wait for five seconds
    time.sleep(5)

pstoryline()

#define all functions
def shining():
    print("Oh no the shining wasn't treasure it is a dangerous sea creature!!!")
    print("This sea creature is unbeatable. It will kill you.")

def cave():
    print("Oh my god!!! You have found the treasure!!!!!")
    print("Congratulations! You have won!")

def winfight():
    print("You and your crew swagger off the pirate ship, your arms overflowing with gloden coins.")
    sail = input("Do you take the course to the glittering horizon or do you smell victory in the depths of the cave?")
    if sail == "glittering horizon":
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
    ship = input("Choose the pirate ship or the dingy.  ")
    if ship == "pirate ship":
        pirateship()
    elif ship == "dingy":
        dingy()
    else:
        print("Incorrect input. Please try again")
        chooseShip()

#call the first function to start story
chooseShip()
