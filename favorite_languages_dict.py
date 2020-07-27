favorite_languages = {
    'jen': ['python','ruby'],
    'sarah': ['c'],
    'edward': ['ruby','go'],
    'phil': ['python','haskell'],
}

#using key,value pairs when using .items() method!!!!
for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are :")
    for language in languages:
        print(f"\t{language.title()}")