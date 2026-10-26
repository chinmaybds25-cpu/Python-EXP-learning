# ============================================================
# SIMPLE CHATBOT - LEVEL 2
# Module 2: Data Structures
# ============================================================

print("=" * 50)
print("           SIMPLE CHATBOT - LEVEL 2")
print("=" * 50)

name = input("Bot: Hello! What is your name? ")

# Dictionary containing chatbot responses
responses = {
    "hello": "Hello! How can I help you?",
    "hi": "Hi! Nice to meet you.",
    "how are you": "I am doing great!",
    "what is your name": "I am SimpleBot.",
    "what can you do": "I can answer simple questions.",
    "help": "Try saying hello, asking my name, or asking how I am.",
    "thank you": "You're welcome!",
    "bye": "Goodbye! Have a nice day."
}

# List to store conversation history
history = []

# Tuple containing supported greetings
greetings = ("hello", "hi", "hey")

# Set containing exit commands
exit_commands = {"bye", "exit", "quit"}

print(f"Bot: Welcome, {name}! Type 'help' for assistance.")

while True:
    user_input = input("\nYou: ").lower().strip()

    history.append(("You", user_input))

    if user_input in exit_commands:
        response = responses["bye"]
        print("Bot:", response)
        history.append(("Bot", response))
        break

    elif user_input in greetings:
        response = responses[user_input]

    else:
        response = responses.get(
            user_input,
            "Sorry, I don't understand. Type 'help' for assistance."
        )

    print("Bot:", response)
    history.append(("Bot", response))

print("\n========== CHAT HISTORY ==========")

for speaker, message in history:
    print(f"{speaker}: {message}")

print("\nTotal messages:", len(history))