#dictionary structure. Always use {} to define dictionary items. Items inside separated by a colon are key/value pairs. 
#Commas separate multiple key/value pairs


# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0['points'])

# countries = {'USA': 'Washington DC', 'France':'Paris', 'England':'London', 'Nigeria':'Abuja'}
# print(countries['France'],countries['USA'])

# assigned_country = countries['USA']
# print(f"The capital of USA is {countries['USA']}")
# countries['Argentina'] = 'Buenos Aires'
# countries['France'] = 'Newark'
# print(countries)

# alien_1 = {}
# alien_1['Color'] = 'Yellow'
# alien_1['Points'] = 15
# alien_1['x'] = 5
# alien_1['y'] = 4
# alien_1['speed'] = 'fast'
# # print(alien_1)

# if alien_1['Color']=='Yellow':
#     print(f"You won {alien_1['Points']} points")
# else:
#     print('No points')

# if alien_1['speed']=='slow':
#     x_increment=1
# elif alien_1['speed']=='medium':
#     x_increment=2
# elif alien_1['speed']=='fast':
#     x_increment=3

# alien_1['x'] = alien_1['x'] + x_increment
# print(alien_1['x'])
# alien_1['Points']=alien_1['Points'] + 5
# print(alien_1['Points'])

# del alien_1['Color']
# print(alien_1)
# alien_1['speed'].upper()
# print(alien_1['speed'].upper())

# # points=alien_1.get('Color','no key found')
# # print(points)

# print(alien_1.get('Color', 'no key'))


'''SIMPLE DICTIONARIES

6-1. Person: Use a dictionary to store information about a person you
know. Store their first name, last name, age, and the city in which
they live. You should have keys such as first_name, last_name, age,
and city. Print each piece of information stored in your dictionary.

6-2. Favorite Numbers: Use a dictionary to store people’s favorite
numbers. Think of five names, and use them as keys in your dictionary.
Think of a favorite number for each person, and store each as a value
in your dictionary. Print each person’s name and their favorite
number. For even more fun, poll a few friends and get some actual data
for your program.

6-3. Glossary: A Python dictionary can be used to model an actual
dictionary. However, to avoid confusion, let’s call it a glossary.

Think of five programming words you’ve learned about in the previous
chapters. Use these words as the keys in your glossary, and store
their meanings as values.

Print each word and its meaning as a neatly formatted output. You might
print the word followed by a colon and then its meaning, or print the
word on one line and then print its meaning indented on a second line.
Use the newline character (\n) to insert a blank line between each
word-meaning pair in your output.
'''

person_1 = {'first_name': 'Frank', 'last_name': 'Jones', 'age': '35', 'city': 'Atlanta'}
print(person_1)

favorite_numbers = {'Alexander': 7, 'Juliet': 11, 'Gabriella': 6, 'Ethan': 9, 'Nick': 14}
print(favorite_numbers)

glossary = {'integer':'number', 'string':'value', 'tuples': 'immutable', 'for loops': 'iterative', 'dictionaries': 'mutable'}
print(f"A tuples is a {glossary['tuples']}")