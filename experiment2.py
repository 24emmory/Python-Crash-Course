players = []
# I FORGOT TO APPEND THE DICTIONARIES TO THE LIST!!!!

player = {'first':'Jean',
          'last':'Ralphio',
          'age': 32,
          'location': 'Pawnee'
}
players.append(player)

player = {'first':'Leslie',
          'last':'Knope',
          'age': 37,
          'location': 'Pawnee'
}
players.append(player)

player = {'first':'Ron',
          'last': 'Swanson',
          'age': 42,
          'location': 'Pawnee'
}
players.append(player)


for player in players:
    full_name = player['first'] + " " + player['last']
    age = str(player['age'])
    location = player['location']

    print(f"{full_name} is {age} and is from {location}")

#commas dont go after every dictionary***
