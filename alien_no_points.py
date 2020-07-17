alien_0 = {'color': 'green', 'speed': 'slow'}

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

#square bracket vs get() method notation
#get() method can set default value with optional second argument, if left blank
#states "none" when returning a value from a key which does not exist.
#use get() method instead of square bracket notation* if unsure* key exists!