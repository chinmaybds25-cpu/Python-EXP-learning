# ============================================================
# SIMPLE CHATBOT - LEVEL 1
# Module 1: Fundamentals and Control Structures
# ============================================================

print("=" * 50)
print("           SIMPLE CHATBOT - LEVEL 1")
print("=" * 50)

name = input("Bot: Hello! What is your name? ")

print("Bot: Nice to meet you,", name)

while True:
    user_input = input("\nYou: ").lower().strip()

    if user_input == "hello" or user_input == "hi":
        print("Bot: Hello! How are you?")

    elif user_input == "how are you":
        print("Bot: I am fine! Thank you.")

    elif user_input == "what is your name":
        print("Bot: I am SimpleBot.")

    elif user_input == "bye" or user_input == "exit":
        print("Bot: Goodbye,", name, "! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand that.")