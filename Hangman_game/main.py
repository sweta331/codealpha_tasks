import random

# ── Word list
WORDS = ["python", "hangman", "science", "rocket", "laptop"]

# ── Hangman visuals (stages 0 – 6) 
HANGMAN_STAGES = [
    "Stage 0",
"Stage 1: O",
"Stage 2: O |",
"Stage 3: O /|",
"Stage 4: O /|\\",
"Stage 5: O /|\\ /",
"Stage 6: O /|\\ / \\"
]
    # 0 wrong guesses
MAX_WRONG = 6   # The player loses after 6 wrong guesses


def display_state(word, guessed_letters, wrong_count):
    """Print the gallows, the word blanks, and the wrong guesses so far."""
    print(HANGMAN_STAGES[wrong_count])

    # Build the word display:  "p _ t h o n"  →  reveals guessed letters
    word_display = " ".join(
        letter if letter in guessed_letters else "_"
        for letter in word
    )
    print(f"\n  Word: {word_display}")
    print(f"  Wrong guesses ({wrong_count}/{MAX_WRONG}): {', '.join(sorted(guessed_letters - set(word))) or '-'}")
    print()


def get_guess(guessed_letters):
    """Ask the player for a single new letter and validate it."""
    while True:
        guess = input("  Guess a letter: ").strip().lower()

        if len(guess) != 1:
            print("  Please enter exactly ONE letter.\n")
        elif not guess.isalpha():
            print("  Only alphabet letters are allowed.\n")
        elif guess in guessed_letters:
            print(f"  You already guessed '{guess}'. Try a different letter.\n")
        else:
            return guess


def play_game():
    """Run one full round of Hangman."""
    word            = random.choice(WORDS)       # Pick a random word
    guessed_letters = set()                      # All letters guessed so far
    wrong_count     = 0                          # Number of incorrect guesses

    print("\n" + "=" * 40)
    print("       Welcome to HANGMAN!")
    print("=" * 40)
    print(f"  The word has {len(word)} letters. Good luck!\n")

    # ── Main game loop ─────────────────────────────────────────────────────────
    while wrong_count < MAX_WRONG:

        display_state(word, guessed_letters, wrong_count)

        # Check win condition BEFORE asking for another guess
        if all(letter in guessed_letters for letter in word):
            print(f"  ✓ You guessed it! The word was '{word}'. You win!\n")
            return

        guess = get_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in word:
            print(f"\n  ✓ Good guess! '{guess}' is in the word.\n")
        else:
            wrong_count += 1
            print(f"\n  ✗ Wrong! '{guess}' is not in the word. ({wrong_count}/{MAX_WRONG} mistakes)\n")

    # ── Player ran out of guesses ──────────────────────────────────────────────
    print(HANGMAN_STAGES[MAX_WRONG])
    print(f"  Game over! The word was '{word}'. Better luck next time!\n")


def main():
    """Entry point — allows the player to play multiple rounds."""
    while True:
        play_game()

        again = input("  Play again? (yes / no): ").strip().lower()
        if again not in ("yes", "y"):
            print("\n  Thanks for playing! Goodbye.\n")
            break


if __name__ == "__main__":
    main()