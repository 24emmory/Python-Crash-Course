daily_agendas = {
    'monday': ['clean car','buy dog food'],
    'tuesday': ['food prep','purchase stocks','buy yacht'],
    'wednesay': ['ininout eats','buy a pressure cooker','clean the dog'],
    'thursday': ['listen to talk radio'],
    'friday': ['regret buying yact', 'realize I know nothing about stocks'],
    'saturday': ['practice python','practice wireshark','eat food'],
    'sunday': ['meditate','go to the dog tracks','meditate'],
}


for days, tasks in daily_agendas.items():
    print(f"\n On {days} I have a lot to do!")
    for task in tasks:
        print(f"\tI have to: {task}")

for days, tasks in daily_agendas.items():
    for day in days:
        print(f"{day}")
        for task in tasks:
            print(f"{tasks}")

# fucking neat! works just as I thought. looping through a string(key) means it goes through every char!

