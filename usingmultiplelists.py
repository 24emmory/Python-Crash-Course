available_toppings = ['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']

requested_toppings = ['mushrooms','french fries','extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping} to pizza")
    else:
        print("Topping not available, sorry.")
print("Pizza finished!")

#using variable defined in list relative to (predefined list) in a check for
#availability against* another list! pretty neat!

available = ['1','2','3','5']

requested = ['1','4','5']

#for item in list desired \n check item against availability - based on resolved
#take two different paths.

for req in requested:
    if req in available:
        print(f"Adding {req} to inventory!")
    else:
        print(f"{req.title()} currently out of stock.")
print("Inventory completed!")