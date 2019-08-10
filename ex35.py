"""branches and functions"""
from sys import exit

def gold_room(): #this is a function
    print("this room is full of gold. How much do you take?")

    choice = input("> ") #this symbol is just to help user to know an input is expected
    if "0" in choice or "1" in choice:
        how_much =int(choice)
    else:
        dead("man, learn to type a number")

    if how_much < 50:
        print("nice, youre not greedy you win!")
        exit(0)

    else:
        dead("you greedy bastard!")

def cthulhu_room():
    print("here you see the great evil cthulu!")
    print("he, it, whatever, stares at you and you go insane")
    print("do you flee for your life or eat your head?")

    choice = input("> ")

    if "flee" in choice:
        start() #call start function

    elif "head" in choice:
        dead("well that was tasty") #call dead function and print message

    else:
        cthulhu_room()  #loop back to top of function

def bear_room():
    print("theres a bear in here")
    print("the bear has a bunch of honey")
    print("the fat bear is in front of another door")
    print("how are you going to move the bear?")

    bear_moved =False
    while True:
        choice = input("< ")

        if choice == "take honey":
            dead("the bear looks at you and then slaps your face off")
        elif choice == "taunt bear" and not bear_moved:
            print("the bear moved away from the door")
            print("you can go through it now")
            bear_moved = True

        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("i got no idea what that means, try 'open door' 'taunt bear' or 'take honey'")




def dead(why):
    print(why + " why good job!")
    exit(0)

def start():
    print("you are in a dark room")
    print("there is a door to your right and left")
    print("which one do you take?")

    choice = input("< ")
    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("you stumble around the room until you starve")


start()
