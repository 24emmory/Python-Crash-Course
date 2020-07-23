#make an empty list for storing aliens.
aliens = []

#make 30 green aliens
for alien in range(30):
    new_alien = {'color':'green','points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

#show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

#show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")

#len(list) total number items in a list
#len(string) total number characters in string

#print(len('dog'))