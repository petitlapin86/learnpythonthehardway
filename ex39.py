"""dictionaries, oh lovely dictionaries"""


things = ['a', 'b', 'c','d'] #this is a dictionary

print(things[1]) #prints b
things[1] = 'z' #changing b to z

print(things[1]) #should print z

states = { #4 states
'Oregon': 'OR',
'Florida': 'FL',
'California' :'CA',
'New York' : 'NY'
}

print(states) #should print 4 states

states['MI'] = 'Michigan' #add a 5th state

print(states) #should print 5 states
