import tkinter as tk

# RULE BASED CHATBOT LOGIC 
def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input:
        return "Hi!"
    elif "how are you" in user_input:
        return "I'm fine, thanks!"
    elif "who are you" in user_input:
        return "I am a rule-based chatbot."
    elif "joke" in user_input:
        return "Why did the computer catch a cold? Because it left its Windows open!"
    elif user_input in ["bye", "goodbye"]:
        return "Goodbye!"
    else:
        return "Sorry, I don't understand."
    
# SEND MESSAGE
def send_message(event=None):
    user_input = entry.get().strip()

    if user_input == "":
        return

    # show user input
    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, "You: " + user_input + "\n")

    # bot response
    response = chatbot_response(user_input)
    chat_log.insert(tk.END, "Bot: " + response + "\n\n")

    chat_log.config(state=tk.DISABLED)
    chat_log.yview(tk.END)

    entry.delete(0, tk.END)

    # exit condition
    if user_input.lower() in ["bye", "goodbye"]:
        root.after(1000, root.destroy)

# GUI setup
root = tk.Tk()
root.title("Basic Chatbot")

chat_log = tk.Text(root, height=20, width=50, state=tk.DISABLED)
chat_log.pack(padx=10, pady=10)

entry = tk.Entry(root, width=40)
entry.pack(pady=5)
entry.focus()

send_btn = tk.Button(root, text="Send", command=send_message)
send_btn.pack()

# Enter key support
entry.bind("<Return>", send_message)

# initial message
chat_log.config(state=tk.NORMAL)
chat_log.insert(tk.END, "Bot: Hello! Type something to chat 😊\n\n")
chat_log.config(state=tk.DISABLED)

# run app
root.mainloop()