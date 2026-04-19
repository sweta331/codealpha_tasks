# 🎮 Hangman Game
```
A simple text-based Hangman game built with Python. Guess the hidden word one letter at a time before the hangman is fully drawn!
```
## 📋 How to Play
1. The game picks a random secret word.
2. You guess one letter at a time.
3. A correct guess reveals that letter in the word.
4. A wrong guess adds a body part to the hangman drawing.
5. You win by guessing all letters before **6 wrong guesses**.
```
## 🚀 How to Run
Make sure Python is installed, then run
```
bash
python hangman.py
```
## 🗂️ Project Structure
hangman.py   →   main game file (all logic is here)
README.md    →   this file
```
## 🧠 Concepts Used
- `random` — picks a random word from the list
- `while` loop — keeps the game running each round
- `if-else` — checks whether a guess is correct or wrong
- `strings` — builds the word display with blanks
- `sets` — tracks guessed letters without duplicates
*Built as a beginner Python project.*