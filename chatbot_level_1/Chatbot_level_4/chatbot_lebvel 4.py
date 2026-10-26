# ============================================================
# SIMPLE CHATBOT - LEVEL 4
# Module 4: OOP and File Handling
# ============================================================

import csv
import os
import random
from datetime import datetime


class SimpleChatbot:

    def __init__(self, name="SimpleBot"):
        self.name = name
        self.history = []
        self.filename = "chat_history.csv"

        self.responses = {
            "hello": ["Hello!", "Hi there!", "Hey!"],
            "hi": ["Hi! How can I help you?"],
            "how are you": ["I am fine!", "I am doing great!"],
            "what is your name": [f"My name is {self.name}."],
            "what can you do": [
                "I can answer simple questions and chat with you."
            ],
            "help": [
                "Try: hello, hi, how are you, what is your name, or bye."
            ],
            "thank you": ["You're welcome!", "Happy to help!"]
        }

    def get_response(self, message):
        """Generate an appropriate response."""

        message = message.lower().strip()

        if message in ["bye", "exit", "quit"]:
            return "Goodbye! Have a nice day."

        possible_responses = self.responses.get(
            message,
            ["Sorry, I don't understand. Type 'help' for assistance."]
        )

        return random.choice(possible_responses)

    def save_message(self, speaker, message):
        """Save conversation messages to a CSV file."""

        file_exists = os.path.isfile(self.filename)

        with open(self.filename, "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            if not file_exists or os.path.getsize(self.filename) == 0:
                writer.writerow(["Timestamp", "Speaker", "Message"])

            writer.writerow([
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                speaker,
                message
            ])

        self.history.append((speaker, message))

    def show_history(self):
        """Display current conversation history."""

        print("\n========== CHAT HISTORY ==========")

        if not self.history:
            print("No messages recorded.")
            return

        for speaker, message in self.history:
            print(f"{speaker}: {message}")

        print("Total messages:", len(self.history))

    def start_chat(self):
        """Start the chatbot."""

        print("=" * 50)
        print("           SIMPLE CHATBOT - LEVEL 4")
        print("=" * 50)

        print(f"{self.name}: Hello! Welcome to the chatbot.")
        print(f"{self.name}: Type 'help' for assistance.")
        print(f"{self.name}: Type 'bye' to end the conversation.")

        while True:
            try:
                user_input = input("\nYou: ").strip()

                if not user_input:
                    print(f"{self.name}: Please enter a message.")
                    continue

                self.save_message("User", user_input)

                response = self.get_response(user_input)

                print(f"{self.name}: {response}")
                self.save_message(self.name, response)

                if user_input.lower() in ["bye", "exit", "quit"]:
                    break

            except (EOFError, KeyboardInterrupt):
                print(f"\n{self.name}: Goodbye!")
                break

            except OSError as error:
                print("File operation error:", error)
                break

        self.show_history()


def main():
    chatbot = SimpleChatbot("SimpleBot")
    chatbot.start_chat()


if __name__ == "__main__":
    main()