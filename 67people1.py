
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

#for loops go through several items and seperate them. The loop runs through until the end of the block,
#then restarts again with the new item.  Usually, we use the assignment operator to help us work with the data
#we find in the lists. So, loop through *this*, while doing so assign these, and then (do whatever you'd like
#with the data

for person in people:
    #name = person['first_name'] +" " + person['last_name'] both work

    name = f"{person['first_name']} {person['last_name']}"
    age = str(person['age'])
    city = person['city']

    print(f"{name} is from {city} and is {age}")