import tkinter as tk
def chatbot_responses(user_input):
    user_input = user_input.lower()

#uses of if-elif
    if user_input == "hello":
        return "Hello there!"
    
    elif user_input == "how are you":
        return "I'm fine, thanks !"
    
    elif user_input == "your name":
        return "I am your chatbot "
    
    elif user_input == "are you AI":
        return "Yes I am an AI"
    
    elif user_input == "That's interesting":
        return "yes"
    
    elif user_input == "bye" or user_input == "goodbye":
        return "Goodbye!"
    
    else:
        return "Sorry, I don't understand that!!."
# using loop
while True:
    user = input("You: ")  
    
    reply = chatbot_responses(user)
    print("Bot:", reply)

    if user.lower() in ["bye", "goodbye"]:
        break