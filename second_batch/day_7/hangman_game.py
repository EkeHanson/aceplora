import random


def choose_word():
    word_list = [
        "apple",
        "banana",
        "cherry",
        "dog",
        "elephant",
        "flamingo",
        "giraffe",
        "hamburger",
        "ice_cream",
        "jacket",
    ]
    return random.choice(word_list)


def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display


def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")

    while True:
        print("\n" + display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            print("Incorrect guess! You have {} attempts left.".format(attempts))

        if display_word(word, guessed_letters) == word:
            print("\nCongratulations! You guessed the word: {}".format(word))
            break

        if attempts == 0:
            print("\nGame over! The word was: {}".format(word))
            break


if __name__ == "__main__":
    hangman()
