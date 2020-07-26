John = {
    'Strength': 10,
    'Dexterity': 20,
    'sayings': ['Booyah','Shimy-ya-ha!']
}

print(f"John has a strength of {John['Strength']},"
      f"a Dexterity of {John['Dexterity']}, and a fist-full"
      f"of American Grit! He also likes talking:")

for saying in John['sayings']:
    print(f"\t{saying}")