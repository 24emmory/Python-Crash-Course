requested_toppings = ['mushrooms','green peppers','extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")

list = ['1','2','3']

for item in list:
    if item == '2':
        print("We are sorry, we are currently out of 2")
    else:
        print(f"Adding {item} to your order!")
print("Your order is finished!")