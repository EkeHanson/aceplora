questions = {
    "Who created Python? ": "A",
    "What year was python created? ":"B",
    "Python is attributed to which comdey group? ": "C",
    "Is the Earth round? ": "A"
}

options = [
    ["A. Guido Van Rossum", "B. Elon Musk", "C. Bill Gates", "D. MArk Zuckerburg"],
    ["A. 1998", "B. 19991", "C. 2000", "D. 2016"],
    ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
    ["A. True", "B. False", "C. Sometimes", "D. What's Earth?" ]
]



def new_game():
    guesses = []
    correct_guesses = 0
    question_number = 1
    for key in questions:
        print(key)
        for i in options[question_number-1]:
            print(i)
        print("__________________________________________")
        guess = input("Enter A, B C or D: ").upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key), guess)
        question_number +=1
    display_score(correct_guesses, guesses)

def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT!!!")
        return 1
    else:
        print("WRONG!!")
        return 0
    
def display_score(correct_guesses, guesses):
    print("_____________________")
    print("RESULTS")
    print("_____________________")
    print("Answers:", end=" ")
    for i in questions:
        print(questions.get(i), end=" ")
    print()
    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int(correct_guesses/len(questions)*100)
    print("Your score is: " + str(score) + "%")

def play_again():
    response = input("Do you want to play again? (Yes or No): ").upper()
    if response == "Yes" or response == "Y":
        return True
    else:
        return False

new_game() 

while  play_again():
    new_game()

print("Thanks for your time!! ")