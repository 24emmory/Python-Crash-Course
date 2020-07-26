Sara = {
    'Speed':29,
    'Cunning': 30,
    'bravery':40,
    'sayings': ['Wompwomp, ya ded','WHY YOU RUNNIN THO?','One tunafish, please!']
}

print(f"Sara is exceptionally mighty, with a speed of {Sara['Speed']}, a cunning of {Sara['Cunning']},"
      f"and a bravery of {Sara['bravery']}. She also has her well known catchy phrases:")

for saying in Sara['sayings']:
    print(f"\t{saying}")