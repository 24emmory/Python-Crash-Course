pets =[]

pet = {
    'name':'pebbles',
    'animal':'dog',
    'owner':'troy',
}
pets.append(pet)

pet = {
    'name':'jack',
    'animal':'dog',
    'owner':'yolanda',

}
pets.append(pet)

pet = {
    'name':'baby',
    'animal':'dog',
    'owner':'jacquelline'

}
pets.append(pet)

#a uniform dictionary name is VERY helpful when looping through, as well as uniformed keys!

for pet in pets:
    print(f"The pet's name is {pet['name'].title()}, the type of pet is a {pet['animal']}, and their owner's "
          f"name is {pet['owner'].title()}")