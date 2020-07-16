current_users_lower = []
for user in current_users:
    current_users_lower.append(user.lower())

vs

newestlistlower = [new.lower() for new in newuserlist]

#The first strategy is appending by creating a new list, using a for loop to go
#through each item in a different list, then within that loop, acting on the
#list using a method to append by calling append and passing throuhg user.lower()

#The second strategy is a list comprehension, which states first the expression
#to use against the data list, which is a for loop of items from a list

