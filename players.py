players = {
    'anaconda': {
        'speed': 'super fast',
        'strength': 'super strong',
        'wisdom': 'aite',
    },

    'Hues': {
        'attitude': 'damn fine',
        'nerves': 'of steel',
        'agility': 'second to none',
    },
}

for name, attribute in players.items():
    print(f"\nName: {name}")
    #full_attribute = f"{attribute_info['']}"
    #Here I realized the shortcomings of the example, it only taught me how to combine uniform
    #keys and values, so if I want to have their keys* and values* displayed on the same line,
    #the way they showed me is not the way. Is there another way to cycle through values without
    #having a uniform name? Will I have to make a for loop for each dictionary of some sort?
    print(f"Attributes: ")
    for at in attribute:
        print(f"\t{at}")

