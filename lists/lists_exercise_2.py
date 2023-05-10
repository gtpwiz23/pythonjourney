'''The following exercises are a bit more complex than those in Chapter 2, but they give you an opportunity to use lists in all of the ways described.
3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? 
Make a list that includes at least three people you’d like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner.
3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. 
You’ll have to think of someone else to invite.
• Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.
• Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
• Print a second set of invitation messages, one for each person who is still in your list.
3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or Exercise 3-5. Add a print() call to the end of your program informing people that you found a bigger dinner table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list.'''

'''Use pop() to remove guests from your list one at a time until only two names remain in your list. 
Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
• Store the locations in a list. Make sure the list is not in alphabetical order.
• Print your list in its original order. Don’t worry about printing the list neatly, just print it as a raw Python list.
• Use sorted() to print your list in alphabetical order without modifying the actual list.
Use reverse() to change the order of your list. Print the list to show that its order has changed.
Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.'''

'''famous_names=['Albert Einstein', 'Isaac Newton', 'Leonardo Da Vinci']
#print(f'{famous_names[0]} you are invited to dinner')
#print(f'{famous_names[2]} cant make the party')
famous_names[2]='Nikola Tesla'
#print(f'{famous_names[2]} you are invited to dinner')
famous_names.insert(0, 'Thomas Edison')
famous_names.insert(2, 'Michelangelo')
famous_names.append('Michael Crichton')
famous_names.pop()
famous_names.pop()
famous_names.pop()
famous_names.pop()
print(famous_names)'''

dream_vacation=['Phuket', 'Bora Bora', 'Bali', 'Maldives', 'New Zealand']
dream_vacation.sort()
print(dream_vacation)