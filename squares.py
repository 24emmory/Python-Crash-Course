for value in range(1, 11):
    value ** 2
    print(value)

#need to assign it to something if i want to work with the NEW value, as it stands, I'm just multiplying a value
print("\n\n\n")

#here, we assined the value we changed so we could use it again in another function, the print function
for value in range(1, 11):
    number = value ** 2
    print(number)

print("\n\n\n")

#here, we assigned the number so we could work with the number. we then appended the number to a list, so
#we could use the list later in another function, print()

squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
#Iwant to use this variable ina list
print(squares)

#practice
newlist = []
for i in range(1,11):
    i1 = i ** 2
    newlist.append(i1)
print(newlist)

#practice2-what am i doing? Im making a range of numbers to work with, im taking the square of each and printing
#them to the screen

for value in range(1,11):
    number = value ** 2
    print(number)
#to make the number evaluation mean anything, I need to assign them to a value, so I may work with the value
#after the script is done
#Good, it works, now, if i wanted to save this number for later, I definitely could by making a list

list = []
#how do I get the items I want in the list?
for value in range(1,11):
    number = value ** 2
    #the only way ive been taught is to append the number. I can do it here as the loop itterates through
    #what we want to do with each value given from the list/range!
    #so, I want to assign the resolved value, good. I printed it before, but now I want to add it to a list
    #this is how
    list.append(number)
    print(list)
    #oops, this prints the list EACH TIME something is added after the append line!

#list = []
#for number in range(1,10):
#    value = number ** 2
#    list.append(value)
#print(list)
# made the one-off-number mistake of not remembering that the range includes the first, but not the last number

list = []
for number in range(1,11):
#loop through each (value) using range function
    value = number ** 2
#current value raised to the second value and assigned to the variable square
    list.append(value)
#each new value* of square is appended to the list of squares
print(list)

list = []
for number in range(1,11):
    #temporary variable
    value = number ** 2
    list.append(value)
print(list)

#omit the temporary variable and append each new value directly
list = []
for number in range(1,11):
    list.append(number ** 2)
    #each value is raised to a 2nd power and immediately appended
print(list)


