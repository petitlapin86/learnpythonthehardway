#
#names variables code and functions

#functions name pieces of code
#they take arguments
#they let you make tiny commands

#you create a function using the def keyword
def print_two(*args):
    arg1, arg2 = args
    print(f"arg 1: {arg1} arg2: {arg2}")
    #okay the above args is actually pointless we can just do this:

def print_two_again(arg1, arg2):
    print(f"arg 1: {arg1} arg2: {arg2}")

def print_one(arg1):
    print(f"this just takes one argument, which is {arg1}")

def print_none():
    print("this takes no arguments")

#
print_two("bananas", "pears")
print_two_again("bananas", "pears")
print_one("pears")
print_none()
