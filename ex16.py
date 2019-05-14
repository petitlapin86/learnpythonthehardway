#exercise 16

#close closes the file
#read reads the contents of the file
#readline reads just one line of a txt file
#truncate empties the file
#wrtie('stuff') writes "stuff" to the file
#seek(0) moves the read/write location to the beginning of the file

from sys import argv

script, filename = argv #when you run in the command line it expects and argument of filename example: python3 ex16.py test.txt

print(f"we're going to erase {filename}.") #it uses the file name argument here
print("If you dont want that hit CTRL-C (^C).") #to quit
print("if you do want that hit, RETURN") #i assume return is a keyword

input("?")

print("opening the file....")
target = open(filename, 'w')

print("truncating the file, goodbye!")
target.truncate()

print("Now im going to ask you three lines")

line1 = input("line 1: ") #whatever the user inputs here will show up in the newly created file
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file")

target.write(line1) #writing the inputed information stored in variables above to the file
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("and finally, we close it")
target.close()
