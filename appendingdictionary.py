dog_list = []

for dog in range(30):
    mansbest = {'speed':'fast','weight':'heavy','happy':'high','loyal':'max',}
    dog_list.append(mansbest)

print(dog_list[:2])
print("...")

print(f"There are currently {len(dog_list)} dogs in our kennel.")
#examle of appendng dictionary to list using range to get many items together