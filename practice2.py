h_letters = []

for letter in 'human':
    h_letters.append(letter)

print(h_letters)

#i want a new set of information, so i create a new list
#use a for loop to act on each value by defining it as a variable
#for variable in list:
#function on each letter
#in this case, the list of values was a STRING!

#form - list.actiononlist(thisvariableadded)

#pretty neat!

#another example would be

list = []
for number in '789':
    list.append(number)
print(f"Why was 6 afraid of 7? Because{list}")
#act on this list "." this functionality (added information)

print("\n\n\n")

#list comprehension line-comprensive list line
h_letters = [ letter for letter in 'human']
print(h_letters)
#identifies when it receives a string or tuple and works on it
#like its a list

lis = []
for item in 'abigail':
    lis.append(item)
print(lis)
