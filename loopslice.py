players = ['charles','martina','michael','florence','eli']

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

#for i in range(1,11):
    #instead of using a range as the element pool in the for loop, the list "players" is used.
    #the for loop targets an element, player, in the list players INSTEAD of an (integer) in a range().
    #first instance of a for loop targeting a list and not a generated range, i believe

cars = ['volvo','corola','honda','ford','tesla']

print("Check out these cars!:")
for car in cars[:3]:
    print(car.title())

#theyre defining the elements in the list each as "car" and this is used later in the loop. Prob. not global defin.

cars = ['volvo,''corola','honda','ford','tesla']
print("Check out these cars!:")
for car in cars[:3]:
    print(car.title())

list = ['item1','item2','item3','item4','item5']
print("Check this out!:")
for lis in list[:3]:
    list.append(lis)
print(list)

