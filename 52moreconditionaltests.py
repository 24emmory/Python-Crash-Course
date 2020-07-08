people = "Troy"
if people == 'Troy':
    print("It's a-me!")



user = 'karen'
new_user = 'Karen'

#print(user == new_user.lower())
#print(user)
#print(new_user.lower())

#testing to find issue. only used { } when replacing variable for value in strin
#g
if (user == new_user.lower()):
    print("User name already taken!")


x = 21
y = 22

if x == y:
    print("Amazn!")
else:
    print("Nope, not equal.")

if x <= y:
    print("X is less than or equal to y")
else:
    print("X is not less than or equal to Y.")

if x >= y:
    print("X is more than or equal to Y.")

if x > y:
    print("X is more than Y.")
else:
    print("X is not more than Y.")

if x < y:
    print("X is less than Y.")
else:
    print("X is not less than Y.")

if True or False:
    print("Logically True!")

x = 0
y = 1
if x > y or x < y:
    print("The or worked!")

if x == 0 and y == 1:
    print("The and worked!")

list = ['lawnchair','fireworks','fans']
if 'fireworks' in list:
    print("'fireworks' is in list!")

if 'friend' not in list:
    print("Ya'll where's David at?")
