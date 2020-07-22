favorite_languages = {
    'jen': 'python',
    'sarah': 'C',
    'edward': 'ruby',
    'phil': 'python',
}

poll_opportunities = ['Troy','jen','jessica','phil']

for people in poll_opportunities:
    if people in favorite_languages.keys():
        print(f"Thank you for taking the poll, {people.title()}!")
    else:
        print(f"Hey, {people.title()}, would you consider taking a quick survey?")

#Just a reminder example of how to use indexes to access values from a list! print(poll_opportunities[0])

#sarah_favorite = favorite_languages['sarah'].title()
#print(f"Sarah's favorite language is {sarah_favorite}!")

#super proud of this one!