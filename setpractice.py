favorite_places = {
    'Sarah':'England',
    'Jessica':'Sofa',
    'Tim':'Class',
    'Daniel': 'Church',
    'Anthony':'England',
}

print("The survey said that people liked visiting these places most:")
for places in set(favorite_places.values()):
    print(places)