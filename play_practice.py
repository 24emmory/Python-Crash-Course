players = {
    'Alfred': {
        'first': 'Al',
        'last': 'Donne',
        'strength': 'High',
        'wisdom': 'medium',
        'speed': 'low',
    },

    'SirBoomBoom': {
        'first': 'Terry',
        'last': 'Boggins',
        'strength': 'High',
        'wisdom': 'Low',
        'speed': 'High',
    },
}
#This is how I access the dict name, just writing the variable holding it. No fancy square brack notation
#What I'm essentially doing here is making a reference call list, I'm breaking apart the players dictionary
#for the purposes of making it easier to access the values held.
#It was uniform, so it's easier to run.

for playername, playerinfo in players.items():
    print(f"\nPlayername: {playername}")
    full_name = f"{playerinfo['first']} {playerinfo['last']}"
    player_strength = playerinfo['strength']
    player_wisdom = playerinfo['wisdom']
    player_speed = playerinfo['speed']
    #assigning makes everything much easier, and some things possible which were not before

    print(f"{full_name}")
    print(f"Strength: {player_strength}")
    print(f"Wisdom: {player_wisdom}")
    print(f"Speed: {player_speed}")

