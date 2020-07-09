alien_color = ['green']

#not =, not is, in! We are checking to see values in list !
#and its if value in list/variable! Not, if variable in value!

#working program, with output
if 'green' in alien_color:
    print("Player has earned 5 points!")

#not working problem, without output
alien_color = ['yellow']
if 'green' in alien_color:
    print("Player has earned 4 points!")
