# Build 3
'''
Postconditions
1 (Welcome): A welcome message is on the console  
2 (user_complaint): user_complaint is the user's response in reply to "Please state your complaint:"
3 (observed_complaint_types): observed_complaint_types = get_complaint_type(user_complaint)
4 (Remedies displayed): the remedies in advice_per_type corresponding to
observed_complaint_types are on the monitor, one line for each.

Example: the user entered “I’ve been saddened by world conflicts,” and the
following is on the console after execution:
Get out more.
Take up a hobby that you love.
Don't expect too much of people.
Don't take offence easily.
'''

complaint_type = ['Depression', 'Human Relations', 'Substance Abuse']
key_words = [['depress', 'sad', 'down'],
             ['conflict', 'argument', 'mistreat', 'quarrel'],
             ['drug', 'alcohol', 'drink', 'cocaine', 'opioid', 'heroin']]
advice_per_type = [
    ['Get out more.', 'Take up a hobby that you love.'],
    ["Don't expect too much of people.", "Don't take offence easily."],
    ['Get counseling.', "Don't delay action on counseling."]]

def get_complaint_type(a_user_complaint):

    my_set = set() # initializes an empty set
    index = 0
    for complaints in key_words: # for getting the sublist of the key_words
        for complaint in complaints:    # for getting the element of the subset
            if complaint in a_user_complaint.lower():
                my_set.add(index)
                break

        index = index + 1
    return my_set

# (Welcome): Postcondition 1
print("Thank you for using Eliza300, a fun therapy program.")

# (user_complaint): Postcondition 2
print("Please state your complaint:")
user_complaint = input()

# (observed_complaint_type): Postcondition 3
observed_complaint_type = get_complaint_type(user_complaint)

# (Remedies displayed): the remedies in advice_per_type corresponding to
#                       observed_complaint_types are on the monitor, one line for each.
if len(observed_complaint_type) > 0:
        for i in range(len(key_words)):
             if i in observed_complaint_type:
                     #print(str(advice_per_type[i]))
                     for element in advice_per_type[i]:
                         print(element)
