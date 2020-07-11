#version one
alien_color = 'yellow'

if 'green' in alien_color:
    print("Player just earned 5 points")
elif 'yellow' in alien_color:
    print("Player just earned 10 points")
elif 'red' in alien_color:
    print("Player just earned 15 points")

#version two
alien_colors = 'purple'

if 'yellow' in alien_colors:
    print("Player has earned 5 points")
elif 'red' in alien_colors:
    print("Player has earned 10 points")
elif 'purple' in alien_colors:
    print("Player has earned 15 points")

#version three
alien_colour = 'orange'

if 'yellow' in alien_colour:
    print("Player has earned 5 points")
elif 'orange' in alien_colour:
    print("Player has earned 10 points")
elif 'pink' in alien_colour:
    print("Player has earned 15 points")