#tracking position of alien that can move different speeds

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

#Move the alien to the right.
#Determine how far to move the alien based on its current speed.

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

print(f"The increment changed is {x_increment}")

#new position is old posit. plus increment
alien_0['x_position'] = alien_0['x_position'] + x_increment

#calling the variable/value number and adding it on the same line as the posit.

#using the assignment operator "=" to reassign the new value of the x_pos key
#value pair in the alien_0 dictionary.

print(f"New position: {alien_0['x_position']}")