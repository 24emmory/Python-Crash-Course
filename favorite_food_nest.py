favorite_foods = {
    'kyle': ['sushi','ramen'],
    'dylan': ['apples'],
    'jon': ['chowmein','dim-sum'],
    'kelly': ['hotdogs','cheese'],
}

#using key,value pairs when using .items() method!!!!
for name, foods in favorite_foods.items():
    print(f"\n{name.title()}'s favorite foods are :")
    for food in foods:
        print(f"\t{food.title()}")