usernames = ['admin','troy','jackie','smith','jerry']

#not if username in usernames, for* username in usernames- to loop through AND
#DEFINE username within for statement!

#if to check /test for value!
for username in usernames:
    if username == 'admin':
        print(f"Hello, {username.title()}, would you like a status report?")
    else:
        print(f"Hello, {username}.")



