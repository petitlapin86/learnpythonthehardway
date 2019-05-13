#parameters, unpacking, variables

from sys import argv
#import is how you add featuress to your script from python modules or libraries

#read the WYSS section for how to run this
script, first, second, third = argv #argv is the argument variable

print(f"The script is called", script)
print(f"your first variable is:", first)
print(f"your second variable is:", second)
print(f"your third variable is:", third)

#to call a program like this in the command line (terminal)
#type python3 ex13.py dumb dumber dumbest
#above i am providing the arguments when i call the file

# this would output
# The script is called ex13.py
# your first variable is: dumb
# your second variable is: dumber
# your third variable is: dumbest
