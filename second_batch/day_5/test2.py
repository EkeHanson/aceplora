# Classwork
# Write a python function that will do the follwoing within the range of 1-30:
# If a number is divisible by 3 it should print("FIZZ")
# If a number is divisible by 5 it should print("BUZZ")
# If a number is divisible by both 3 and 5 it should print ("FIZZBUZZ") to the terminal


def divisibility():
    for i in range(1, 31):
        if (i % 3 == 0) and i % 5 == 0:
            print(str(i), ": FIZZBUZZ")
        elif i % 3 == 0:
            print(str(i), ": FIZZ")
        elif i % 5 == 0:
            print(str(i), ": BUZZ")


divisibility()
