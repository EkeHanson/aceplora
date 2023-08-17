# Function: This is a block of code that will only be executed when it is called


# def hello():
#     print("Hello World")


# hello()


def main():
    operation = input(
        "Please select your operation: A for Addition, D for division and  S subtraction: "
    ).upper()
    if operation == "A":
        addition()
    elif operation == "S":
        subtraction()
    elif operation == "D":
        division()


def addition():
    num1 = int(input("Please enter the first number here: "))
    num2 = int(input("Please enter the econd number here: "))
    print(num1 + num2)


def subtraction():
    num1 = int(input("Please enter the first number here: "))
    num2 = int(input("Please enter the econd number here: "))
    print(num1 - num2)


def division():
    num1 = int(input("Please enter the first number here: "))
    num2 = int(input("Please enter the econd number here: "))
    print(num1 / num2)


main()
