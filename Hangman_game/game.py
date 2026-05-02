import random

WORDS = ["python", "hangman", "game", "aeroplane", "mouse"]

def start_game():
    return {
        "word": random.choice(WORDS),
        "guessed": [],
        "wrong": 0
    }

def process_guess(state, guess):
    word = state["word"]

    if guess and guess not in state["guessed"]:
        state["guessed"].append(guess)

        if guess not in word:
            state["wrong"] += 1

    display = " ".join([l if l in state["guessed"] else "_" for l in word])

    win = all(l in state["guessed"] for l in word)
    lose = state["wrong"] >= 6

    return state, display, win, lose