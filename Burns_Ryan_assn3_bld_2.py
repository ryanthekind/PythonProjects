# Eliza300
# Intent: A list of helpful actions that a troubled person could take. Build 2

possible_actions = ['taking up yoga', 'sleeping eight hours a night', 'relaxing', 
        'not working on weekends', 'spending two hours a day with friends']

'''
Precondition: possible_actions is the list defined above

Postconditions:

1. (Welcome): A welcome message is on the console

2. (user_complaint): user_complaint is the user's response to
"Please describe your emotional complaint--in one punctuation-free line: "

3. (how_long): how_long is the user's string response to
"How many months (between 1 and 99) have you experienced ...?"

4. (Month validity): EITHER how_long has the requested form
OR this terminated AND "Sorry, illegal input. Eliza is quitting; run Eliza again."
is on the console

5. (Advice):
EITHER how_long < 3 AND "Please return in * months" is on the console where *
is 3-how_long
OR how_long >= 3 AND The phrases in possible_action are on separate lines
on the console, each preceded by "Try ".
'''
#precondition
possible_actions = ['taking up yoga.', 'sleeping eight hours a night.', 'relaxing.', 
        'not working on weekends.', 'spending two hours a day with friends.']

#postconditions

#1
welcome = "Thank you for sing Eliza300, a fun therapy program."
print(welcome)

prompt = "Please describe your emotional complaint--in one punctuation-free line:"
print(prompt)

#2
user_complaint = input();

reaction = "How many months (between 1 and 99) have you experienced "   
print(reaction + "'" + user_complaint + "'?")

#3
how_long = int(input())

#4 month validity and advice
if (how_long >=3) and (how_long < 100):
    print(how_long , "months is significant. Sorry to hear it.")
    
    for advice in possible_actions:
        print("Try" , advice)

elif (how_long < 3) and (how_long > 0):
    print("Please return in" , 3 - how_long  , "months")
    
else:
    print("Sorry, illegal input. Eliza is quitting; run Eliza again.")
        

import sys
sys.exit()

