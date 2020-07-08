my_foods = ['pizza','falafel','carrot cake']

#Definitely does not work
friend_foods = my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')


print(my_foods)
print(friend_foods)

#supposed to work
list = ['1','2','3','4']

list1 = list[:-1]
#everything but the last one, off by one
print(list)
print(list1)