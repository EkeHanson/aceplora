import random

def choose_word():
    words = ["python", "hangman", "programming", "computer", "keyboard", "developer", "game", "challenge"]
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed = ""
    for letter in word:
        if letter in guessed_letters:
            displayed += letter
        else:
            displayed += "_"
    return displayed

def hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts_left = 6

    print("Welcome to Hangman!")
    print(display_word(word_to_guess, guessed_letters))

    while True:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed this letter.")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print("Correct!")
        else:
            attempts_left -= 1
            print("Incorrect!")

        print(display_word(word_to_guess, guessed_letters))
        print(f"Attempts left: {attempts_left}")

        if "_" not in display_word(word_to_guess, guessed_letters):
            print(f"Congratulations! You've guessed the word '{word_to_guess}'.")
            break

        if attempts_left == 0:
            print(f"Sorry, you've run out of attempts. The word was '{word_to_guess}'.")
            break

if __name__ == "__main__":
    hangman()
