# The if statement is used to execute a block of code if the condition is True:
# The conditional operators: <, >, >=, <=, ==, and != are used 
age = int(input("Please enter your age: "))
if age >= 18:
    print("You are not an adult!")
elif age == 0:
    print("You have not been born yet")
elif age < 18:
    print("You are a child")
else:
    print("What are you?")
