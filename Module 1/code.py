# Simple Chatbot
# Utility 1 - Python Programming Lab
# Module 1: Fundamentals of Python / Control Structures

def chatbot_response(user_input):
    """Return an appropriate response for the user's input."""

    user_input = user_input.lower().strip()

    # Greetings
    if user_input in ["hello", "hi", "hey"]:
        return "Hello! Nice to meet you."

    elif user_input == "good morning":
        return "Good morning! Have a great day."

    elif user_input == "good afternoon":
        return "Good afternoon! How can I help you?"

    elif user_input == "good evening":
        return "Good evening! How can I help you?"

    # Common questions
    elif user_input == "how are you":
        return "I am fine. Thank you for asking!"

    elif user_input == "what is your name":
        return "My name is PythonBot."

    elif user_input == "who created you":
        return "I was created as a Python Programming Lab project."

    elif user_input == "what can you do":
        return "I can answer predefined questions and respond to greetings."

    elif user_input == "what is python":
        return "Python is a high-level, interpreted programming language."

    elif user_input == "thank you" or user_input == "thanks":
        return "You're welcome!"

    # Exit commands
    elif user_input in ["bye", "exit", "quit"]:
        return "Goodbye! Have a nice day."

    # Unknown input
    else:
        return "Sorry, I don't understand that. Please try another question."


def main():
    """Main function of the chatbot."""

    print("=" * 45)
    print("        WELCOME TO PYTHON CHATBOT")
    print("=" * 45)
    print("Type 'bye', 'exit', or 'quit' to end the chat.")
    print()

    while True:
        user_input = input("You: ")

        response = chatbot_response(user_input)

        print("Bot:", response)

        # Stop the chatbot when exit command is entered
        if user_input.lower().strip() in ["bye", "exit", "quit"]:
            break


# Program execution
main()
