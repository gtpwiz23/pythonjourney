"""Write a short program that prompts a user to enter his/her name, use
the input() function to collect user input in a variable, generate an
output stating how pleased you are to meet the user(the output should
use the variable that holds the user's name to print a message to the
user). Finally output the length of the user's name with the len()
function.
NB: You can push this code to github and I'll find your repository to
review your submission.
Use the following commands to add file changes to your git working
tree and push the updated version of the code to github(No.1 below is
more of an instruction and not a command):
1. Make sure you are in the pythonjourney directory and not a subdirectory
2. Do * git status *
3. Do * git add .*
4. Do * git commit -m 'your_commit_message' *
5. Do * git push -u origin main *"""

print ('Please type your name in the line below')
x=input()
print('Nice to meet you' +', ' + x)
print(len(x))