#python doesnt require an else block at the end of an if-elif chain!
#Sometimes it's useful to include an else block, sometimes its better to use
#an additional elif statement that "catches the specific condition of interest"
#"Catching the specific condition of interest"

age = 12

if age < 4:
    price = 0

elif age < 18:
    price = 25

elif age < 65:
    price = 40

elif age >= 65:
    price = 20

#it's a bit cleaner to use an elif to catch the specific condition of interest*
#instead of an else, we just covered all other possible numbers with a more
#than or equal to 65!