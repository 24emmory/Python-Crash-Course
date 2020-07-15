current_users = ['Fin', 'jannet', 'admin', 'jon', 'Dan']
new_users = ['Louis', 'Jannet', 'Karen', 'dan', 'Laura']

current_users_lower = []
for user in current_users:
    current_users_lower.append(user.lower())

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print("Sorry " + new_user + ", that name is taken.")
    else:
        print("Great, " + new_user + " is still available.")


current_users_lower = []
for user in current_users:
    current_users_lower.append(user.lower())
