players = {
    'anaconda': {
        'speed': 'speed: super fast',
        'strength': 'strength: super strong',
        'wisdom': 'wisdom: aite',
    },
#tried repeating stat* through the three atributes of anaconda, but only the last ome, wisdom showed
#up in the loop. keys of the same name in the same dict are of issue. in the example,
#they used the same key names, but in diffrrent dicts!
    'Hues': {
        'attitude': 'attitude: damn fine',
        'nerves': 'nerves: of steel',
        'agility': 'agility: second to none',
    },
}

#for name, attribute in players.items():
#    print(f"\nName: {name}")

#same outcome
#for name in players.keys():
#    print(f"\nName: {name}")

print("Name: Anaconda")
names = players['anaconda']
for key, value in names.items():
    print(f"\t{value}")


#to access and loop through the values I desire, I have  to target the dicts independently
#proud of self for using the assignment operator to access a dict in a dict to use items.
#could have done the same wih square bracket notation, will have to test. sq brack and value method***

#same outcome
#for value in names.values():
#    print(f"\t{value}")

print("Name: Hues")
names2 = players['Hues']
for key, value in names2.items():
    print(f"\t{value}")

#I couldnt figure out how to get the name of a dict inside of a dict, unfortunately.
#tried pretty hard. Happy with what I came up with, though.