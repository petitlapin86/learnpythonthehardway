"""dictionaries, oh lovely dictionaries"""


things = ['a', 'b', 'c','d'] #this is a dictionary

print(things[1]) #prints b
things[1] = 'z' #changing b to z

print(things[1]) #should print z

states = { #4 states
'Oregon': 'OR',
'Florida': 'FL',
'California' :'CA',
'New York' : 'NY',
'Michigan' : 'MI'
}

print(states) #should print 4 states

states['MI'] = 'Michigan' #add a 5th state

print(states) #should print 5 states


cities = {
'CA' : 'San Francisco',
'MI' : 'Detroit',
'FL': 'Jacksonville'
}

print("Michigans abbreviation is: ", states['Michigan'])

print("Michigan has the City: ", cities[states['Michigan']])

print("*" *10) #print a star dividing line

for abbrev, city in list(cities.items()): #iterate through allm items in list
    print(f"{abbrev} has the city {city}") #print first item and then second item 
