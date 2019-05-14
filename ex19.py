#different ways to use and call functions

def cheese_and_crackers(cheese_count, boxes_of_crackers): #this is my function it takes two arguments
        print(f"You have {cheese_count} cheeses!")
        print(f"You have {boxes_of_crackers} boxes of crackers!")
        print("man thats enough for a party")
        print("invite some friends!")

print("we can just give the function numbers directly:")
cheese_and_crackers(20, 30)

print("Or we can use variables from our script:")
amount_of_cheeses = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheeses, amount_of_crackers)

print("we can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

print("and we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheeses + 100, amount_of_crackers + 10)
