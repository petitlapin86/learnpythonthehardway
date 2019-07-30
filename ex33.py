"""while loops"""

i = 0 #count starts at zero

numbers = []  #empty list

while i < 6:
    print(f"at the top i is {i}")
    numbers.append(i)

    i = i + 1 # add one to i or i+=1
    print("numbers now: ", numbers)
    print(f"at the bottom i is {i}")

print("the numbers: ")  #this is outside of the while loop so prints at the end
for num in numbers:
    print(num)
