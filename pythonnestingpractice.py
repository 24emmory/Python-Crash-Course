#make an empty list for storing cats
cats = []

#make 30 green cats
for cat_number in range (30):
    new_cat = {'color':'green','speed':'fast','food':'fish'}
    cats.append(new_cat)

for cat in cats[:3]:
    if cat['color'] == 'green':
        cat['color'] = 'yellow'
        cat['speed'] = 'slow'
        cat['food'] = 'pasta'

for cat in cats[:5]:
    print(cat)