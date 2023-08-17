import tkinter as tk
import random

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")

        self.words = ["python", "hangman", "programming", "computer", "keyboard", "developer", "game", "challenge"]
        self.word = random.choice(self.words)
        self.guesses = []
        self.attempts = 6

        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.pack()

        self.word_display = tk.Label(root, text="_ " * len(self.word), font=("Helvetica", 20))
        self.word_display.pack()

        self.attempts_display = tk.Label(root, text=f"Attempts left: {self.attempts}", font=("Helvetica", 12))
        self.attempts_display.pack()

        self.input_label = tk.Label(root, text="Enter a letter:", font=("Helvetica", 12))
        self.input_label.pack()

        self.input_entry = tk.Entry(root)
        self.input_entry.pack()

        self.submit_button = tk.Button(root, text="Submit", command=self.check_guess)
        self.submit_button.pack()

    def update_display(self):
        display_word = ""
        for letter in self.word:
            if letter in self.guesses:
                display_word += letter + " "
            else:
                display_word += "_ "
        self.word_display.config(text=display_word)

    def check_guess(self):
        guess = self.input_entry.get().lower()
        self.input_entry.delete(0, tk.END)

        if len(guess) != 1 or not guess.isalpha():
            tk.messagebox.showinfo("Invalid Input", "Please enter a single letter.")
            return

        if guess in self.guesses:
            tk.messagebox.showinfo("Repeated Guess", "You've already guessed this letter.")
            return

        self.guesses.append(guess)
        self.update_display()

        if guess not in self.word:
            self.attempts -= 1
            self.attempts_display.config(text=f"Attempts left: {self.attempts}")
            if self.attempts == 0:
                tk.messagebox.showinfo("Game Over", f"Sorry, you've run out of attempts. The word was '{self.word}'.")
                self.root.destroy()
                return

        if all(letter in self.guesses for letter in self.word):
            tk.messagebox.showinfo("Congratulations", f"Congratulations! You've guessed the word '{self.word}'.")
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
