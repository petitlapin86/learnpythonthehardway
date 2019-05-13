#more variables and printing


my_name = 'Paige'
my_age = 32 #int variable
my_height = '5 foot 5 inches' #string variable
my_weight = 115 #pounds
my_eyes = 'Green'
my_teeth = 'White'
my_hair = 'Auburn'

#these are example of output
#using the new f instead of .format(name) style
print(f"Lets talk about {my_name}.")
print(f"She's {my_height} tall.")
print(f"She's {my_weight} pounds.")
print(f"She has {my_eyes} eyes and {my_hair} hair")
print(f"Her teeth are usually {my_teeth} depending on the coffee")

total = my_age + my_weight
print(f"If I add {my_age} to {my_weight}, I get {total}.")
