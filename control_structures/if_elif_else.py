# control statements (e.g. if, elif, else)

'''5-3. Alien Colors #1: Imagine an alien was just shot down in a game.
Create a variable called alien_color and assign it a value of 'green',
'yellow', or 'red'.

Write an if statement to test whether the alien’s color is green. If
it is, print a message that the player just earned 5 points.

Write one version of this program that passes the if test and another
that fails. (The version that fails will have no output.)

5-4. Alien Colors #2: Choose a color for an alien as you did in
Exercise 5-3, and write an if-else chain.

If the alien’s color is green, print a statement that the player just
earned 5 points for shooting the alien.

If the alien’s color isn’t green, print a statement that the player
just earned 10 points.

Write one version of this program that runs the if block and another
that runs the else block.'''

# alien_color='blue'

# if alien_color=='blue':
#     print('you earned five points')
# else:
#      print('you earned ten points')

'''5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into
an if-elif- else chain.

If the alien is green, print a message that the player earned 5 points.

If the alien is yellow, print a message that the player earned 10 points.

If the alien is red, print a message that the player earned 15 points.

Write three versions of this program, making sure each message is
printed for the appropriate color alien.'''

# alien_color='black'

# if alien_color=='green':
#     print('you earned five points')
# elif alien_color=='yellow':
#     print('you earned ten points')
# else:
#      print('you earned fifteen points')
    

''' 5-6. Stages of Life: Write an if-elif-else chain that determines a
person’s stage of life. Set a value for the variable age, and then:

If the person is less than 2 years old, print a message that the
person is a baby.

If the person is at least 2 years old but less than 4, print a message
that the person is a toddler.

If the person is at least 4 years old but less than 13, print a
message that the person is a kid.

If the person is at least 13 years old but less than 20, print a
message that the person is a teenager.

If the person is at least 20 years old but less than 65, print a
message that the person is an adult.

If the person is age 65 or older, print a message that the person is an elder.'''

# age=25
# if age<2:
#     print('person is a baby')
# elif age <4:
#     print('person is a toddler')
# elif age <13:
#     print('person is a kid')
# elif age <20:
#     print('person is a teenager')
# elif age<65:
#     print('person is an adult')
# elif age>=65:
#     print('person is an elder')



# grocery_list=['milk','eggs','bread','fruit','vegetables']
# if 'eggs' in grocery_list:
#     print('It exists')
#     if 'milks' in grocery_list:
#         print('we have milk')
#     else:
#         print('we dont have milk')


# year=2024
# if year < 1900:
#     print('in the past')
# elif year < 2000:
#     print('20th century')
# elif year < 2023:
#     print('current year')
# else:
#     print('no year found')

# grocery_list=['butter', 'blackberries', 'apples', 'cheese', 'pickles', 'meat']

# if 'butter' in grocery_list:
#     print('we have butter')
# elif 'blackberries' in grocery_list:
#     print('we have bberries')
# # else:
# #     print('we dont have those items')


# pizza_toppings=['cheese', 'pepperoni', 'tomato', 'basil', 'mushroom']
# if 'souya' in pizza_toppings:
#     print('added cheese')
# if 'pepperoni' in pizza_toppings:
#     print('added pepperoni')
# if 'tomato' in pizza_toppings:
#     print('added tomato')
# if 'basil' in pizza_toppings:
#     print('added basil')


'''5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of independent 
if statements that check for certain fruits in your list.
• Make a list of your three favorite fruits and call it favorite_fruits.
• Write five if statements. Each should check whether a certain kind of fruit is in your list. 
If the fruit is in your list, the if block should print a statement, such as You really like bananas!'''

favorite_fruits=['apples', 'strawberries', 'bananas', 'blueberries', 'kiwi']
# if 'apples' in favorite_fruits:
#     print ('You really like apples')
# if 'bananas' in favorite_fruits:
#     print ('You really like bananas')
# if 'blackberries' in favorite_fruits:
#     print ('You really like blackberries')
# if 'kiwi' in favorite_fruits:
#     print ('You really like kiwi')
# if 'grapes' in favorite_fruits:
#     print ('You really like grapes')
# if favorite_fruits:
#     print('list of favorite fruits')

# available_fruits=['oranges', 'raspberries', 'lemons', 'mango', 'pineapple', 'grapefruit', 'bananas', 'blueberries']

# #for loop iterates through the strings in the lists favorite_fruits. The if statement checks the strings in available_fruits and prints 'purchase fruit'
# #if there's a match. Otherwise, the else statement prints fruits that aren't in both lists.
# for fruit in favorite_fruits:
#     if fruit in available_fruits:
#         print(f'purchase fruit' + ' = ' + f'{fruit}')
#     else:
#         print(f'dont purchase fruit{fruit}')
    
'''USING IF STATEMENTS WITH LISTS

5-8. Hello Admin: Make a list of five or more usernames, including the
name 'admin'. Imagine you are writing code that will print a greeting
to each user after they log in to a website. Loop through the list,
and print a greeting to each user:

If the username is 'admin', print a special greeting, such as Hello
admin, would you like to see a status report?

Otherwise, print a generic greeting, such as Hello Jaden, thank you
for logging in again.'''

# users=['admin', 'user1', 'user2', 'user3']
# # for username in users:
# #     if username!='admin':
# #         print(f'Welcome {username}')
# #     else: 
# #         print('Hello admin')

# if len(users)>0:
#     print('We have users')
#     for username in users:
#         if username!='admin':
#             print(f'Welcome {username}')
#         else: 
#             print('Hello admin')
# else:
#     print('We need to find some users!')

'''5-9. No Users: Add an if test to hello_admin.py to make sure the list
of users is not empty.

If the list is empty, print the message We need to find some users!

Remove all of the usernames from your list, and make sure the correct

message is printed.'''




'''5-10. Checking Usernames: Do the following to create a program that simulates

how websites ensure that everyone has a unique username.

Make a list of five or more usernames called current_users.

Make another list of five usernames called new_users. Make sure one or

two of the new usernames are also in the current_users list.

Loop through the new_users list to see if each new username has
already been used. If it has, print a message that the person will
need to enter a new username. If a username has not been used, print a
message saying that the username is available.

Make sure your comparison is case insensitive. If 'John' has been
used, 'JOHN' should not be accepted. (To do this, you’ll need to make
a copy of current_users containing the lowercase versions of all
existing users.)'''

# current_users=['user1', 'user2', 'user3', 'user4', 'user5']
# current_users2=[current_users.lower() for current_users in current_users]
# new_users=['user6', 'user7', 'user8', 'user9', 'user5']
# for users in new_users:
#     if users.lower() in current_users2:
#         print('A new username is required')
#     else:
#         print('Username is available')


'''5-11. Ordinal Numbers: Ordinal numbers indicate their position in a
list, such as 1st or 2nd. Most ordinal numbers end in th, except 1, 2,
and 3.

Store the numbers 1 through 9 in a list.

Loop through the list.

Use an if-elif-else chain inside the loop to print the proper ordinal
end- ing for each number. Your output should read "1st 2nd 3rd 4th 5th
6th 7th 8th 9th", and each result should be on a separate line.'''

ordinals=[1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in ordinals:
    if number==1:
        print('1st')
    elif number==2:
        print('2nd')
    elif number==3:
        print('3rd')
    elif number==4 or 5 or 6 or 7 or 8 or 9:
        print(f'{number}'+ 'st')
