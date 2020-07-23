dogs = []

for dog in range(10):
    mansfriend = {'fur':'golden','weight':'heavy','speed': 4}
    dogs.append(mansfriend)

#forgot to do square bracket notation first on the lines below if, and then noticed the if line without
#the square bracket notation. I need to specify using square bracket notation, and remember the power of splice
#splicing in narrowing things down
for dog in dogs[:3]:
    if dog['fur'] == 'golden':
        dog['fur'] = 'black'
        dog['weight'] = 'light'
        dog['speed'] = 10
#if dogs['fur'] == 'golden: is wrong because im referencing the list WHILE specifying the dog variable!
#im mentioning a wider variable once ive already specified past it. Checking the singular dictionary dog,
#not the list!

#^same thing happened when using assignment operator, used the list of dictionaries and not the actual dictionary
# ex) dogs (list of dict) vs dog (actually dictionary id like to work with , seperated from list by a splice!)

#use splices to specify what to change! further specification, same methodology with the for/if statements
#for this huge list (within this space of splice), if condition met, act
for dog in dogs[:5]:
    print(dog)

    #using splices to specify dictionary items in list, be sure to ref the dictionary(item), and not the list
    #to work on! the goal here was to work on the items individually, not the entire list. pretty neat!