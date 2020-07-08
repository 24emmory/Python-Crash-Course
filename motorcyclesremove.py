list = ['frank','olga','dan']

print(f"Hey, {list[0].title()}, would you like to come to dinner? How about you, {list[1].title()}? I'm sure we could get {list[2].title()} to come. That guy's a great writer!")

print(list)
print(len(list))



firstpop = list.pop(1)
print(f"Unfortunately, {firstpop.title()} can't make it today.")
print(len(list))

list.append('David')
print(list)
print(len(list))


print(f"We, fortunately, have revised our current list to reflect who has RSVP'd. {list[0].title()}, would you be able to take time away from your family to sit with us? Hey, {list[1].title()}, can you make it tonight? We would love to hear your stories. How about you, {list[2].title()}, would you like to catch up?")

print("Hey ya'll! Quick update, we found ourselves a bigger table! We can accomodate more people, now!")

#adding new gues at the beginning, middle, and end of list

list.insert(0,'John')
print(list)
print(len(list))

list.insert(2,'Peggie')
print(list)

list.insert(-1,'Brian')
print(list)
print(len(list))

print(f"Hey, {list[0].title()}, would you stop being so blue and godlike and come visit?")

print(f"{list[1].title()}, would you leave nirvana for a moement to sit to have dinner with us?")

print(f"{list[2].upper()}! What are you doing with that brute, come out this way for a bite!")

print(f"Mr {list[3].title()} Harmon, come by this evening to regail us with witty anecdotes, if you would!")

print(f"Hey, {list[4].upper()} get over here for food")

print(f"{list[-1].title()}, come down for eats.")

print(f"I'm so sorry, we only have room for two guests at the dinner, the table will not be here in time.")

print(list)

pop1 = list.pop(5)
print(f"Hey, {pop1}, let's catch up another time!")
print(len(list))

pop2 = list.pop(0)
print(f"Hi {pop2}, unless you can materialize a table, don't come!")
print(len(list))

pop3 = list.pop(1)
print(f"Maybe another time, {pop3}")
print(len(list))

pop4 = list.pop(-1)
print(f"Get outtaaa here, {pop4}!")
print(len(list))

print(list)

print(f"{list[0].title()}, I'm looking forward to catching up with you, jichan.")
print(len(list))

print(f"I'm looking forward to hear your amazing stories, {list[-1].title()} Harmon")
print(list)
del list[1]
print(len(list))

del list[0]
print(len(list))
print(list)