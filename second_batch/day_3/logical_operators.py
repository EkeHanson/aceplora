# Logical operators are used to check if two or more condtional statements are True
# Logical operators are : 'and' , 'or' and 'not'
# For the 'and' logical operator the both sides must be True
# For the 'or' logical operator at least one side must be True for the statement to be True
# For 'not' logical operator is used to change True to False and False to True
has_good_credit_history = True
has_integrity = False

if has_good_credit_history and not has_integrity:
    print("He/She is eligible for loan")