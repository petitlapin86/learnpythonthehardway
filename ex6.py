#strings and text

types_of_people = 10

x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't" # you can use a single quote inside a double quote and vice versa. however a double quotation of the same type as you used for the string will create an issue.
y = f"Those who know {binary} and those who {do_not}"

print(x) #printing one variable
print(y)

print(f"I said: {x}") #printing a variable within a string
print(f"I also said: {y}")

hilarious = False #giving a boolean value
joke_evaluation = "Isn't that joke so funny!? {}"

print(joke_evaluation.format(hilarious)) #showing the .format() version

w = "this is the left side of..."
e = "a string with a right side"

print(w + e) #showing how to print multiple variables at once
