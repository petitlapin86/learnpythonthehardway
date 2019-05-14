#functions and files
#to run this in the comman line type: python3 ex20.py test.txt
from sys import argv #importing argv module from sys library

script, input_file = argv #takes an argument of a file and stores in a variable

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file) #takes input file and stores in a new variable and opens it = this seems repetitive?

print("first lets print the whole file \n")

print_all(current_file) #printing the whole file

print("now lets rewind kind of like a tape \n")

rewind(current_file)

print("lets print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
