# names = {'name1':'Alexander', 'name2': 'Nick', 'name3':'Chubi', 'name4': 'Mike', 'name5': 'John'}
# continent_names = {'continent1': 'Asia', 'continent2': 'Africa', 'continent3': 'North America',
#                    'continent4': 'Europe', 'continent5': 'Antartica'}
# car_brands = {'brand1': 'Audi', 'brand2': 'ferrari', 'brand3': 'bmw', 'brand4':'ford', 'brand5':'Mercedez'}

# list_names = [names, continent_names, car_brands]
# # print(list_names[0].values())
# # names_dictionary = list_names[0]
# # print(names_dictionary['name4'])
# print(list_names[0:2])

# new_list = []
# new_list.append(list_names[0])
# new_list.append(list_names[2])

# print(new_list)

# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'blue', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}
# alien_3 = {'color': 'black', 'points': 20}
# alien_4 = {'color': 'orange', 'points': 25}
# alien_5 = {'color': 'brown', 'points': 30}

# # Loop through the aliens list. Find any alien whose color is green and replace the color with indigo and points with 50. 

# aliens = [alien_0, alien_1, alien_2, alien_3, alien_4, alien_5]
# for alien in aliens:
#     if alien['color']=='green':
#         alien ['color'] = 'indigo'
#         alien ['points'] = 50
    
# print(aliens[0])

# pizza = {
#     'crust': 'thick',
#     'toppings': ['pepperoni', 'cheese']
# }

# for topping in pizza['toppings']:
#     print(topping)


# pizza = {'topping': 'cheese', 'crust': ['thin', 'thick']}

# for crust_types in pizza['crust']:

#     print(f'This pizza is {crust_types}')



# for crust_type in pizza['crust']:
#     print(crust_type)


# print(pizza['toppings'][1])

# pizza_toppings = pizza['toppings']
# print(pizza_toppings[1])


# favorite_langauges = {
#   'Nick': ['python', 'C'],
#   'Chubi': ['python', 'javascript'],
#   'Ethan': ['C', 'Assembly']
#   }

# for languages in favorite_langauges['Chubi']:
#     print(languages)

# for names, languages in favorite_langauges.items():
#     print(f'{names} really likes to program in {languages}')

'''6-7. People:Make three new dictionaries representing different people, and store all three dictionaries in a list called people. 
    Loop through your list of people. As you loop through the list, print everything you know about each person.'''

# person1_dictionary = {'person1': 'joe', 'person2': 'jane', 'person3': 'jason'}
# person2_dictionary = {'person4': 'mike', 'person5': 'mary', 'person6': 'moe'}
# person3_dictionary = {'person7': 'sam', 'person8': 'susan', 'person9': 'steve'}
# persons = [person1_dictionary, person2_dictionary, person3_dictionary]
# for person in persons:
#     print(person)
    

'''6-8. Pets: Make several dictionaries, where each dictionary represents a differ- ent pet. In each dictionary, 
include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. 
Next, loop through your list and as you do, print everything you know about each pet.'''

pet_dictionary_1 = {'owner': 'Nick', 'pet': 'dog'}
pet_dictionary_2 = {'owner': 'Mike', 'pet': 'cat'}
pet_dictionary_3 = {'owner': 'Sam', 'pet': 'bird'}

pets = [pet_dictionary_1, pet_dictionary_2, pet_dictionary_3]

for pet in pets:
    print(pet)
					
'''6-9. Favorite Places: Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary, 
and store one to three favorite places for each person(you can store the favorite places as a list).  Loop through the dictionary, 
and print each person’s name and their favorite places. '''

favorite_places = {'mike':'beach', 'steve':['mountains', 'park'], 'larry': ['library', 'forest', 'home']}
for people, places in favorite_places.items():
    print(people, places)



