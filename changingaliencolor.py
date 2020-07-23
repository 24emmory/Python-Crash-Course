aliens = []
#list to store new aliens

for alien_number in range(30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)

#challenging part is figuring out names for the variables and lists!
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
        #using assignment operator and equality operators to pick the first four aliens out and change their
        #properties

for alien in aliens[:5]:
    print(alien)
print("...")
#using a slice to print the first five aliens
#note: slices are not affected by the off by one error so often seen