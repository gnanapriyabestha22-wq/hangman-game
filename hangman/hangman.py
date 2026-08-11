
import tkinter as tk
import random

# -----------------------------
# List of words
# -----------------------------

words = [
    "apple", "banana", "orange", "mango", "grape",
    "python", "computer", "keyboard", "network",
    "developer", "algorithm", "database", "software"
]

# -----------------------------
# Hangman stages
# -----------------------------

hangman_stages = [
    """
    -----
    |   |
    O   |
   /|\\  |
   / \\  |
        |
    --------
    """,
    """
    -----
    |   |
    O   |
   /|\\  |
   /    |
        |
    --------
    """,
    """
    -----
    |   |
    O   |
   /|\\  |
        |
        |
    --------
    """,
    """
    -----
    |   |
    O   |
   /|   |
        |
        |
    --------
    """,
    """
    -----
    |   |
    O   |
    |   |
        |
        |
    --------
    """,
    """
    -----
    |   |
    O   |
        |
        |
        |
    --------
    """,
    """
    -----
    |   |
        |
        |
        |
        |
    --------
    """
]


# -----------------------------
# Variables
# -----------------------------

word = ""
display = []
guessed_letters = []
attempts = 6


# -----------------------------
# Start / Restart Game
# -----------------------------

def start_game():
    global word, display, guessed_letters, attempts

    word = random.choice(words)
    display = ["_"] * len(word)
    guessed_letters = []
    attempts = 6

    # Enable entry and button
    guess_entry.config(state="normal")
    guess_button.config(state="normal")

    # Clear input
    guess_entry.delete(0, tk.END)

    # Update screen
    hangman_label.config(text=hangman_stages[attempts])
    word_label.config(text=" ".join(display))
    guessed_label.config(text="Guessed Letters: ")
    attempts_label.config(text="Attempts Left: 6")
    result_label.config(text="Make your guess! 🎯")


# -----------------------------
# Check Guess
# -----------------------------

def check_guess():
    global attempts

    guess = guess_entry.get().lower()
    guess_entry.delete(0, tk.END)

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        result_label.config(
            text="❌ Please enter only one alphabet."
        )
        return

    # Duplicate guess
    if guess in guessed_letters:
        result_label.config(
            text="⚠️ You already guessed that letter."
        )
        return

    guessed_letters.append(guess)

    # Correct guess
    if guess in word:

        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess

        result_label.config(
            text="✅ Correct Guess!"
        )

    # Wrong guess
    else:
        attempts -= 1

        result_label.config(
            text="❌ Wrong Guess!"
        )

    # Update screen
    hangman_label.config(text=hangman_stages[attempts])
    word_label.config(text=" ".join(display))
    guessed_label.config(
        text="Guessed Letters: " + " ".join(guessed_letters)
    )
    attempts_label.config(
        text=f"Attempts Left: {attempts}"
    )

    # Check win
    if "_" not in display:
        result_label.config(
            text="🎉 Congratulations! You Won!"
        )
        guess_entry.config(state="disabled")
        guess_button.config(state="disabled")

    # Check game over
    elif attempts == 0:
        result_label.config(
            text=f"💀 Game Over! The word was: {word}"
        )
        guess_entry.config(state="disabled")
        guess_button.config(state="disabled")


# -----------------------------
# Create Window
# -----------------------------

window = tk.Tk()

window.title("🎮 Hangman Game")
window.geometry("600x700")

# -----------------------------
# Title
# -----------------------------

title_label = tk.Label(
    window,
    text="🎮 HANGMAN GAME",
    font=("Arial", 24, "bold")
)

title_label.pack(pady=20)


# -----------------------------
# Hangman Drawing
# -----------------------------

hangman_label = tk.Label(
    window,
    text="",
    font=("Courier", 16),
    justify="left"
)

hangman_label.pack()


# -----------------------------
# Word
# -----------------------------

word_label = tk.Label(
    window,
    text="",
    font=("Arial", 24, "bold")
)

word_label.pack(pady=20)


# -----------------------------
# Attempts
# -----------------------------

attempts_label = tk.Label(
    window,
    text="Attempts Left: 6",
    font=("Arial", 14)
)

attempts_label.pack(pady=5)


# -----------------------------
# Guessed Letters
# -----------------------------

guessed_label = tk.Label(
    window,
    text="Guessed Letters:",
    font=("Arial", 14)
)

guessed_label.pack(pady=5)


# -----------------------------
# Result
# -----------------------------

result_label = tk.Label(
    window,
    text="Make your guess! 🎯",
    font=("Arial", 16, "bold")
)

result_label.pack(pady=15)


# -----------------------------
# Input Box
# -----------------------------

guess_entry = tk.Entry(
    window,
    font=("Arial", 18),
    width=5,
    justify="center"
)

guess_entry.pack(pady=5)


# -----------------------------
# Guess Button
# -----------------------------

guess_button = tk.Button(
    window,
    text="GUESS",
    font=("Arial", 14, "bold"),
    width=12,
    command=check_guess
)

guess_button.pack(pady=10)


# -----------------------------
# Restart Button
# -----------------------------

restart_button = tk.Button(
    window,
    text="🔄 PLAY AGAIN",
    font=("Arial", 13, "bold"),
    width=15,
    command=start_game
)

restart_button.pack(pady=10)


# -----------------------------
# Start Game
# -----------------------------

start_game()

# Run Tkinter
window.mainloop()
