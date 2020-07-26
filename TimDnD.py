Tim = {
    'Wisdom': 50,
    'Magicstuff': 50,
    'Arcane-ness': 50,
    'name' : ['The great who-ha','The wizard formerlly known as "the great who-ha"','Tim']
}

print(f"This magus is known for his greatness! With a wisdom at {Tim['Wisdom']}, a magicstuff at "
      f"{Tim['Magicstuff']}, and an Arcane-ness at {Tim['Arcane-ness']}, he's an animal!"
      f"He also goes by many names:")

for name in Tim['name']:
    print(f"\t{name}")