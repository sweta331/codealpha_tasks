import tkinter as tk

# chatbot logic 
def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input:
        return "Hello there!"
    elif "who are you" in user_input:
        return "I am a chatbot"
    elif user_input == "joke":
        return "okay : Why did the computer catch a cold? Because it left its Windows open!"
    elif user_input == "that's funny":
        return "Yes!"
    elif user_input in ["bye", "goodbye"]:
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that!"

# send message function
def send_message():
    user_input = entry.get()
    chat_log.insert(tk.END, "You: " + user_input + "\n")

    response = chatbot_response(user_input)
    chat_log.insert(tk.END, "Bot: " + response + "\n\n")

    entry.delete(0, tk.END)

# GUI setup for chatbot
root = tk.Tk()
root.title("Chatbot")

chat_log = tk.Text(root, height=20, width=50)
chat_log.pack()

entry = tk.Entry(root, width=50)
entry.pack()

send_btn = tk.Button(root, text="Send", command=send_message)
send_btn.pack()

root.mainloop()