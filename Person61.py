person = {'first_name':'Troy','last_name':'Oshima','age':29,'city':'Long Beach'}

#using square bracket to access values
print(person['first_name'])
#using get() method to access values of a key-value pair in a dictionary(KVP)
practice = person.get('last_name','No last name assigned')
print(practice)
print(person['age'])
practice2 = person.get('city', 'No city assigned')
print(practice2)