
people = []

person =   {'first_name':'Troy',
           'last_name':'Oshima',
           'age':29,
           'city':'Long Beach',
           }
people.append(person)

person =   {'first_name': 'Derek',
           'last_name':'Hoggins',
           'age':32,
           'city': 'Los Angeles'
            }
people.append(person)

person =   {'first_name': 'Jennifer',
           'last_name': 'Ramirez',
           'age': 28,
           'city': 'El Monte'
           }
people.append(person)


for person in people:

    name = f"{person['first_name']} {person['last_name']}"
    age = f"{str(person['age'])}"
    city = f"person['city']"

    print(f"{name} is from {city} and is {age}")
    #format string works fine in assignment, as well as just using sq brac notation and "+" syntax
    #exercise in understanding
