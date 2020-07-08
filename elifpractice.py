#add as many elif blocks in code as you'd like!

age = 12

if age < 4:
    price = 0

elif age < 18:
    price = 25

elif age < 65:
    price = 40

else:
    price= 20

#another try

age = 65
if age < 4:
    status = 'toddler'

elif age < 12:
    status = 'child'

elif age < 19:
    status = 'teenager'

elif age < 35:
    status = 'young adult'

elif age < 51:
    status = 'adult'

else:
    status = 'senior'

print(f"Your status is considered: {status.title()}")
