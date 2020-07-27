favorite_games = {
    'Anthony': ['pacman','halo','diablo 2'],
    'Gal': ['wonderwoman','sims'],
    'John': ['halo 2','overwatch'],
    'Richard': ['starcraft 2','Goose Game'],
}

for name, games in favorite_games.items():
    print(f"\n{name.title()}'s favorite games are :")
    for game in games:
        print(f"\t{game.title()}")