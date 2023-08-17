# Loop gives us the ability to do something again and again
#while loop
# for loop

# while loop

# name = ""
# while len(name) == 0:
#     name = input("Please enter your name: ")
# print("Hello", name)

# i = 0
# while i < 10:
#     print("i is less than 10")

# a =  1
# while a < 10:
#     print("Meow " * a)
#     # a = a + 1
#     a += 1

#FOR LOOP
#The for loop is a statement that will execute its block of code a limited number of times
            #[first, last, step]
# for i in range(5):
#     print(i)

# for i in range(5,10):
#     print(i)

# for i in range(5,15,2):
#     print(i)

import time

for i in range(10,0,-1):
    print(i)
    time.sleep(1)
print("Happy New year!!!")

# ASSIGNEMENT
# write your own count down timer from 20 to 0 and and the eend diplay "Happy New Month" 
# Note: Your timer should sleep for 0.5 seconds