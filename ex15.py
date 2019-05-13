#this is showing how to use arguments to pull in other files, open and read them 
from sys import argv

script, filename = argv #use argv to get a file name

txt = open(filename) #opens a file

print(f"heres your file {filename}!")
print(txt.read()) #calls the read function using dot notation to read the file

print("type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
