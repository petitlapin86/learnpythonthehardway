"""doing things to lists"""


ten_things = "Apples oranges crows telephone lights sugar"

print("wait there are not 10 things in that list, lets fix that")

stuff = ten_things.split(' ') #creating a new list, splitting between spaces
more_stuff = ["day", "night", "song", "frisbee", "corn", "banana", "girl", "boy"]

while len(stuff) != 10: #while the length of stuff list is less than 10 run this block of code
    next_one = more_stuff.pop() #create list next one and add an item from more_stuff to it
    print("adding: ", next_one) #display the list item added
    stuff.append(next_one) #add next_one list to stuff list
    print(f"there are {len(stuff)} items now") #display the number of items

print("there we go: ", stuff)

print("lets do some things with stuff")

print(stuff[1]) #accesses second item on list (lists start at 0)
print(stuff[-1]) #accesses last item on  list
print("whoah fancy!")
print(stuff.pop()) #pulls the last item on the list
print(' '.join(stuff)) #joins list into one string

print('#'.join(stuff[3:5])) #prints only selected list elements with a # sign between themgit 
