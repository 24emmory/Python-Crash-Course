favorite_languages = {
    'Jerry':'Hamburger',
    'Tatiana':'Sushi',
    'Clover':'Tomatoes',
    'Paris':'Cheese',
}

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, that sounds deicious!")
    print(f"{favorite_languages[name].title()} would hit the spot right now!")


    #sorting the keys as they're returned* in the for loop