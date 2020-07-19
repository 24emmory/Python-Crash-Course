favorite_languages = {
    'jen': 'python',
    'sarah': 'c' ,
    'edward': 'ruby' ,
    'phil': 'python' ,
}

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        print(f"\t{name.title()}, I see you love {favorite_languages[name].title()}!")

        #alternative to using an assignment operator to simplify us using a key
        #the key we used initially after using the keys() method, to pull a
        #value
#in line 9, that's where we tell the program we want to use keys, and that name
#would be the name holding the value of each key used