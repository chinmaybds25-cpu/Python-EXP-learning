# ============================================================
# SIMPLE CHATBOT - LEVEL 3
# Module 3: Functions and Exception Handling
# ============================================================

import random


def get_response(user_input):
    """Generate a response based on user input."""

    user_input = user_input.lower().strip()

    responses = {
        "hello": ["Hello!", "Hi there!", "Hey!"],
        "hi": ["Hi!", "Hello! How can I help?"],
        "how are you": [
            "I am fine. Thank you!",
            "I am doing great!",
            "I am ready to chat!"
        ],
        "what is your name": ["I am SimpleBot."],
        "what can you do": [
            "I can answer simple questions and chat with you."
        ],
        "help": [
            "Try: hello, how are you, what is your name, or bye."
        ],
        "thank you": ["You're welcome!", "Happy to help!"]
    }

    if user_input in ["bye", "exit", "quit"]:
        return "Goodbye! Have a nice day."

    return random.choice(
        responses.get(
            user_input,
            ["Sorry, I don't understand. Type 'help' for assistance."]
        )
    )


def chat():
    """Run the chatbot conversation."""

    print("=" * 50)
    print("           SIMPLE CHATBOT - LEVEL 3")
    print("=" * 50)

    name = input("Bot: Hello! What is your name? ").strip()

    if not name:
        name = "Friend"

    print(f"Bot: Nice to meet you, {name}!")
    print("Bot: Type 'help' for commands or 'bye' to exit.")

    while True:
        try:
            user_input = input("\nYou: ").strip()

            if not user_input:
                print("Bot: Please enter a message.")
                continue

            response = get_response(user_input)
            print("Bot:", response)

            if user_input.lower() in ["bye", "exit", "quit"]:
                break

        except (EOFError, KeyboardInterrupt):
            print("\nBot: Goodbye!")
            break

        except Exception as error:
            print("Bot: An unexpected error occurred:", error)


if __name__ == "__main__":
    chat()