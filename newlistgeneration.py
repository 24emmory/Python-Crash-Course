
strategies = []

for strat_number in range (10):
    new_strat = {'speed':10,'strength':3,'cunning':8}
    strategies.append(new_strat)

for new_strat in strategies:
    if new_strat['speed'] == 10:
        new_strat['speed'] = 20
        new_strat['strength'] = 8
        new_strat['cunning'] = 22

for new_strat in strategies[:1]:
    print(new_strat)

