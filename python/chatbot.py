from datetime import datetime

# ==========================================
# SIMPLE CHATBOT USING PYTHON
# ==========================================

# Module 1: Basic Chatbot and Control Structures

def main():

    bot_name = "PyBot"
    user_name = ""

    # Module 2: Predefined Responses
    responses = {
        "hello": "Hello! How can I help you?",
        "hi": "Hi there! Nice to meet you.",
        "hey": "Hey! How are you?",
        "how are you": "I am fine, thank you!",
        "what is your name": "My name is PyBot.",
        "who created you": "I was created using Python.",
        "what can you do":
            "I can answer predefined questions and greetings.",
        "what is python":
            "Python is a high-level programming language.",
        "what is a variable":
            "A variable stores a value in a program.",
        "what is a dictionary":
            "A dictionary stores data in key-value pairs.",
        "what is a function":
            "A function is a reusable block of code.",
        "what is a loop":
            "A loop repeats a block of code.",
        "what is artificial intelligence":
            "Artificial Intelligence enables computers to perform "
            "tasks that normally require human intelligence.",
        "tell me a joke":
            "Why do programmers prefer dark mode? "
            "Because light attracts bugs!",
        "motivate me":
            "Keep learning and improving. Small steps lead to success!",
        "thank you": "You're welcome!",
        "thanks": "Happy to help!",
        "good morning": "Good morning! Have a wonderful day.",
        "good afternoon": "Good afternoon! How can I help?",
        "good evening": "Good evening! Welcome to PyBot.",
        "good night": "Good night! Take care.",
        "bye": "Goodbye! Have a nice day."
    }

    # Module 2: Conversation History
    history = []

    # Module 3: Functions

    def show_welcome():
        print("\n" + "=" * 50)
        print("          WELCOME TO PYBOT")
        print("=" * 50)
        print("I am PyBot, your simple Python chatbot.")
        print("Type 'help' to see available commands.")
        print("=" * 50)

    def show_menu():
        print("\n------------ CHATBOT MENU ------------")
        print("1. Start chatting")
        print("2. View predefined questions")
        print("3. View conversation history")
        print("4. Display conversation statistics")
        print("5. Save conversation to a file")
        print("6. Exit")
        print("--------------------------------------")

    def show_questions():
        print("\n------ AVAILABLE QUESTIONS ------")

        for question in responses:
            print("-", question)

        print("--------------------------------")

    def get_response(message):
        nonlocal user_name

        # String methods
        message = message.strip().lower()

        if message == "":
            return "Please enter a message."

        if message in ("bye", "exit", "quit"):
            return "Goodbye! Have a nice day."

        if message == "help":
            return (
                "You can greet me, ask Python questions, "
                "request a joke, or view the menu."
            )

        if message.startswith("my name is "):
            entered_name = message[len("my name is "):].strip()

            if entered_name:
                user_name = entered_name.title()
                return f"Nice to meet you, {user_name}!"

            return "Please enter your name."

        if message == "what is my name":
            if user_name:
                return f"Your name is {user_name}."

            return "I do not know your name yet."

        if message in ("hello", "hi", "hey") and user_name:
            return f"Hello, {user_name}! How can I help?"

        # Conditional statements and dictionary lookup
        if message in responses:
            return responses[message]

        return (
            "Sorry, I don't understand that question yet. "
            "Type 'help' for assistance."
        )

    def chat():
        print("\nStart chatting with PyBot.")
        print("Type 'back' to return to the main menu.")

        while True:
            user_message = input("\nYou: ").strip()

            if user_message.lower() == "back":
                print("Returning to the main menu.")
                break

            bot_message = get_response(user_message)

            print(f"{bot_name}: {bot_message}")

            # Store messages in a list of dictionaries
            history.append({
                "user": user_message,
                "bot": bot_message,
                "time": datetime.now().strftime(
                    "%d-%m-%Y %H:%M:%S"
                )
            })

            if user_message.lower() in ("bye", "exit", "quit"):
                break

    def show_history():
        print("\n--------- CONVERSATION HISTORY ---------")

        if not history:
            print("No conversation history available.")
        else:
            for number, item in enumerate(history, start=1):
                print(f"\nConversation {number}")
                print("Time:", item["time"])
                print("You:", item["user"])
                print("PyBot:", item["bot"])

        print("----------------------------------------")

    def show_statistics():
        total = len(history)
        understood = 0

        for item in history:
            if "Sorry, I don't understand" not in item["bot"]:
                understood += 1

        print("\n--------- CHATBOT STATISTICS ---------")
        print("Total messages:", total)
        print("Recognized responses:", understood)
        print("Unrecognized responses:", total - understood)
        print("-------------------------------------")

    def save_history():
        try:
            with open("chat_history.txt", "w", encoding="utf-8") as file:
                file.write("PYBOT CONVERSATION REPORT\n")
                file.write("=" * 40 + "\n")
                file.write(
                    "Generated on: "
                    + datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                    + "\n\n"
                )

                if not history:
                    file.write("No conversations recorded.\n")

                for number, item in enumerate(history, start=1):
                    file.write(f"Conversation {number}\n")
                    file.write("Time: " + item["time"] + "\n")
                    file.write("User: " + item["user"] + "\n")
                    file.write("PyBot: " + item["bot"] + "\n")
                    file.write("-" * 40 + "\n")

            print("Conversation saved to chat_history.txt")

        except OSError as error:
            print("Unable to save the file:", error)

    # Module 4: Complete Chatbot Main Menu

    show_welcome()

    while True:
        show_menu()

        try:
            choice = input("Enter your choice (1-6): ").strip()

            if choice == "1":
                chat()

            elif choice == "2":
                show_questions()

            elif choice == "3":
                show_history()

            elif choice == "4":
                show_statistics()

            elif choice == "5":
                save_history()

            elif choice == "6":
                print("\nThank you for using PyBot!")
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please select 1 to 6.")

        except (KeyboardInterrupt, EOFError):
            print("\nChatbot stopped. Goodbye!")
            break


# Start the program
if __name__ == "__main__":
    main()