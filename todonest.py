daily_agendas = {
    'monday': ['clean car','buy dog food'],
    'tuesday': ['food prep','purchase stocks','buy yacht'],
    'wednesay': ['ininout eats','buy a pressure cooker','clean the dog'],
    'thursday': ['listen to talk radio'],
    'friday': ['regret buying yact', 'realize I know nothing about stocks'],
    'saturday': ['practice python','practice wireshark','eat food'],
    'sunday': ['meditate','go to the dog tracks','meditate'],
}

#defining keys and values using a for loop and items. for loops accesses&puts the values into the key-pair
#when item is called. item tells for* that it's a key value pair
for days, tasks in daily_agendas.items():
    print(f"\n On {days} I have a lot to do!")
    for task in tasks:
        print(f"\tI have to: {task}")


#practicing/trying things out
for day in days:
    print(f"The day is {day}")

#I discovered that the list is considered a value, so we need to use semi colons
#Also, we need to use a for loop in conjunction with items() method to assign/put values from-
#- the dictionary's key-value pairs
#an ex of this is - for key, value in list.items()*needed when accessing values in this way
#I also discovered we can loop through the values* if they're a list, but if we loop through-
#-the keys, we only get one letter out from the word we're on

love = {'christmas':['donkey','lobster','taiwan'],
}
for holiday, things in love.items():
    for h in holiday:
        print(f"{h}")
    for t in things:
        print(f"{t}")