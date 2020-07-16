current_users = ['eric', 'willie', 'admin', 'erin', 'Ever']
new_users = ['sarah', 'Willie', 'PHIL', 'ever', 'Iona']

#need a modified copy of code, assign it all in one line
current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print("Sorry " + new_user + ", that name is taken.")
    else:
        print("Great, " + new_user + " is still available.")

current_users_lower = []
for user in current_users:
    current_users_lower.append(user.lower())

print("\n \n \n")
#expression to apply to data set (variables in list)
#current_users_lower = [user.lower() for user in current_users]

old_users = ['troy','jackie','andrew','chris']
newest_users = ['dan','andrew','Troy']

newest_lower_users = [user.lower() for user in newest_users]

for new in newest_lower_users:
    if new in old_users:
        print("Sorry, username " + new + " already taken.")
    else:
        print("Congratulations, username " + new + " is available.")