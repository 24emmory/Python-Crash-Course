
people = [{'first_name':'Troy',
           'last_name':'Oshima',
           'age':29,
           'city':'Long Beach'
           },

          {'first_name': 'Derek',
           'last_name':'Hoggins',
           'age':32,
           'city': 'Los Angeles'},

          {'first_name': 'Jennifer',
           'last_name': 'Ramirez',
           'age': 28,
           'city': 'El Monte'
           }]

#had to research syntax for this, it's a normal list syntax, but what I was trying was to name every dict
#vs this approach of just listing out each dict in a list.
#Need to think on this a minute

for person in people:
    print(f"{people}")