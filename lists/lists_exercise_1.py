"""3-1. Names: Store the names of a few of your friends in a list called names. 
Print each person’s name by accessing each element in the list, one at a time.
3-2. Greetings: Start with the list you used in Exercise 3-1, 
but instead of just printing each person’s name, print a message to them. 
The text of each mes- sage should be the same, but each message should be personalized with the person’s name.
Methods:
.append(‘new_name’), .insert(1, ‘new_name’), .remove('name'), del names[0], names.pop(), names.sort(), print(sorted(names))"""

names = ['Chubi', 'Hatem', 'Sam', 'Alexander', 'Syed']

names[0]='Frank'
names.append('Mike')
names.insert(3, 'Ethan')
names.remove('Ethan')
names.pop(0)
print(sorted(names))
