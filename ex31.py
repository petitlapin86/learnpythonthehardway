"""making decisions"""


print("""you enter a dark toom with two doors.
do you go through door #1 or door door #2?""")


door = input("> ")  #this symbol doesnt mean anything its just being used to indicate to the user where to type their response

if door == "1":
    print("there is a giant bear here eating a cheese cake")
    print("what do you do?")
    print("1. Take the cake")
    print("2. Scream at the bear")

    bear = input("> ")

    if bear == "1":
        print("the bear eats your face off. Good Job!")
    elif bear == "2":
        print("the bear eats your legs off. good job!")
    else:  #in this case anything they enter other than 1 or 2 will end here
        print("well doing {bear} is probably better.")
        print("bear runs away")

elif door == "2":
    print("you stare into the endless abyss at cthulhu's retina")
    print("1. blueberries")
    print("2. yellow jacket clothespins")
    print("3. understanding revolvers yelling melodies")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("your body survives powered by a mind of jello")
        print("good job")
    else:
        print("the insanity rots your eyes into a pool of muck")
        print("good job!")

else:
    print("you stumble around and fall on a knife and die.")
