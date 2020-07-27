dictionary = {
    'key' : 'value',
}

for key, value in dictionary.items():
    print(f"{key}")
    for v in value:
        print(f"{v}")

#I KNEW IT!!! when you loop through dict key- val pairs, it loops through the individual strings as keys!