rivers = {'nile':'egypt',
          'mississippi':'america',
          'Yangtze':'china',
          }

#loop through printing rivers and countries in dictionary
for river, country in rivers.items():
    print(f"The river {river.title()} runs through the country of {country.title()}")

#loop through printing rivers in dictionary
for river in rivers.keys():
    print(river)

#lopp through printing countries in dictionary
for country in rivers.values():
    print(country)

#example of square bracket notation
print(rivers['nile'])
