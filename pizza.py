#storing info using dictionary instead of a list

pizza = {
    'crust':'thick',
    'toppings': ['mushrooms','extra cheese'],
}

#summarized
print(f"You ordered a {pizza['crust']}-crust pizza "
      "with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")
