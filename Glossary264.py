glossary = {'tuples':'unchangeable lists','key_value_pair':'used in dictionaries'
            ,'square_bracket_notation':'used to get a value from a key-value',
            'get_method':'used to get a value from a key-value','elif_chain':
            'used to execute precise conditions','set':'a collection in which each item must be unique','values()':
            'A method we use to iterate through just the values of the dictionary','keys() method':
            'A method we use to iterate through just the keys in a dictionary','items() method':
            'a method we use to create two variables which returns a list of key-value pairs','get() method':
            'used when unsure if there will or will not be a key to access values- gives def/created respnse'}
#get() used as follows
#alien_0 = {'color':'green','speed':'slow"}

#point_value = alien_0.get('points','no point value assigned.')
#print(point_value)
#author loves usinga assign operator to assign method output i've noticed. assign for method output/easily usable

for key, value in glossary.items():
    print(f"\nThese are the items in the dictionary glossary: \n Key:{key} Value:{value}")
