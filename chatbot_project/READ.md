# Python Chatbot

A simple chatbot built with Python that uses functions, loops, input/output, and `if` / `elif` conditionals to respond to basic user messages.

## Features

- Uses a function to generate chatbot responses
- Reads user input from the console with `input()`
- Uses `if`, `elif`, and `else` to select replies
- Uses a loop to keep the chat running until the user says `bye` or `goodbye`
- Prints output to the console with `print()`

## How it works

1. The chatbot reads user text using `input("You: ")`.
2. The text is converted to lowercase.
3. A function checks the message using `if`, `elif`, and `else`.
4. The function returns a reply string.
5. The reply is printed with `print("Bot:", reply)`.
6. A `while True` loop keeps the conversation running until the user types `bye` or `goodbye`.

## Usage

1. Open a terminal in the project folder.
2. Run the chatbot with:

```bash
python main.py
```

3. Type a message and press Enter.
4. The bot will respond until you say `bye` or `goodbye`.

## Example conversation

```
You: hello
Bot: Hello there! 👋
You: how are you
Bot: I'm fine, thanks !
You: your name
Bot: I am your chatbot 🤖
You: bye
Bot: Goodbye! 👋
```

## Notes

- The main program uses two chatbot response functions in `main.py`.
- Each function uses `if` / `elif` branches to match user input.
- The loop ensures the chat continues until the exit words are entered.
