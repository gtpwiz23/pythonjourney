# items method is used to extract key/value pairs from dictionary lists.
# items returns both key and values (two variables should be defined to store both items), keys and values methods are specific.
# a set is a collection of unique items. The set command used to call values ommits duplicates. 

# countries = {'USA': 'Washington DC', 'Argentina':'Paris', 'England':'London', 'Nigeria':'Abuja', 'France':'Paris'}
# # for key,value in countries.items():
# #     print(f"The following information displays country and capital: {key} = {value}")

# for capitals in set (countries.values()):
#     print(capitals)


# LOOPING THROUGH A DICTIONARY

# 6-5. Rivers: Make a dictionary containing three major rivers and the
# country each river runs through. One key-value pair might be 'nile':
# 'egypt'.

# Use a loop to print a sentence about each river, such as The Nile runs
# through Egypt.

# Use a loop to print the name of each river included in the dictionary.

# Use a loop to print the name of each country included in the dictionary.

# 6-6. Polling: Use the code in favorite_languages.py

# Make a list of people who should take the favorite languages poll. Include

# some names that are already in the dictionary and some that are not.

# Loop through the list of people who should take the poll. If they have
# already taken the poll, print a message thanking them for responding.
# If they have not yet taken the poll, print a message inviting them to
# take the poll.

# rivers = {'Egypt': 'Nile', 'Brazil':'Amazon', 'USA': 'Mississippi'}
# # for country,river_name in rivers.items():

#     # print(f"The {river_name} runs through {country}")

# for river in rivers.values():
#     print(river)

# for country in rivers.keys():
#     print(country)

languages = {'James':'Go', 'Nick':'Python', 'Chubi': 'Python', 'Steve': 'Java'}

friends = ['Hatem', 'John', 'Nick', 'Steve', 'James', 'Chubi']

for name in friends:
    if name in languages.keys():
        print(f'Thank you for taking the poll {name}')
    else:
        print(f'Please take the poll {name}')