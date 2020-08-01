aliens = []

for alien_num in range(30):
    newalien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(newalien)

#for loop is more vertical than just a print loop, couldnt manage a vert spread even using "\n{}"
for alien in aliens[:5]:
    print(alien)