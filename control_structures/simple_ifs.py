#if statements can be used to validate whether a condition is true or false. It can be used with other boolean commands (e.g. 'and' 'or' 'in' 'not in' '<=>' and '!=')

"""5-1. Conditional Tests: Write a series of conditional tests. Print a
statement describing each test and your prediction for the results of
each test. Your code should look something like this:

                  car = 'subaru'
                  print("Is car == 'subaru'? I predict True.")
                  print(car == 'subaru')

                  print("\nIs car == 'audi'? I predict False.")
                  print(car == 'audi')

Look closely at your results, and make sure you understand why each
line evaluates to True or False.

Create at least ten tests. Have at least five tests evaluate to True
and another five tests evaluate to False."""


# cars='BMW'
# trucks='Mercedez'
# if cars=='ford'.title():
#     print('hello world')
# if cars!='Ford':
#     print("does not exist")

# cars='BMW'
# trucks='Mercedez'
# if cars=='BMW'and trucks!='Mercedez':
#     print('Both cars exist')

# big_number=99
# small_number=2
# if big_number>98 or small_number>=3:
#     print('numbers are big and small')

grocery_list=['milk','eggs','bread','fruit','vegetables']
if 'eggs' in grocery_list:
    print('It exists')
    if 'milks' in grocery_list:
        print('we have milk')
    else:
        print('we dont have milk')

# is_active=False 
# if is_active:
#     print("It's true")

# europe_country='France'
# print('I predict this is false')
# print(europe_country!='France')

# triple_digit_number=105
# print('I predict this is true')
# print(triple_digit_number<105)