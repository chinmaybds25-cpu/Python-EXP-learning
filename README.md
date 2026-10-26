Simple Chatbot Using Python — Python Experiential Learning Utility

Name: Chinmay Prashant Bhojne 
USN: CD25079
Branch / Section: CSE-DS (B), Semester III
Course: Python Programming Lab (N-PCCCD304P)
Institute: S. B. Jain Institute of Technology, Management & Research, Nagpur
Course Coordinator: Ms. Ashwini Yerlekar

1. Utility Overview

A Simple Chatbot built in Python that interacts with users by responding to predefined questions, greetings, and commands. The program accepts user input continuously, identifies keywords or messages, and provides suitable responses. It also includes a menu-driven interface, conversation history, basic statistics, and an option to save the conversation to a text file.

The utility has been developed in four levels, so that each level maps directly onto a module of the Python Programming Lab syllabus and grows from a basic interactive program into a complete chatbot application.

2. Level-wise Development Plan

Level| Syllabus Module| What is added at this level| File
Level 1| Module 1 — Fundamentals & Control Structures| Basic chatbot using variables, input/output, if/elif/else, while and for loops, break/continue, predefined greetings, and an exit command.| "level1_module1/chatbot_level1.py"
Level 2| Module 2 — Data Structures| A dictionary of predefined responses, lists for conversation history, tuples for storing conversation entries, sets for unique user queries, string methods, slicing, and a menu-driven interface.| "level2_module2/chatbot_level2.py"
Level 3| Module 3 — Functions| Complete modular chatbot using user-defined functions, default and keyword arguments, multiple return values, "*args", lambda expressions, "map()", "filter()", recursion for menu handling, and exception handling using "try/except/else/finally" and "raise".| "level3_module3/chatbot_level3.py"
Level 4| Module 4 — NumPy & Pandas (+ Module 5 — File Handling & OOP)| Chatbot and conversation-management classes using OOP, inheritance and encapsulation, permanent conversation storage in a CSV file, analysis of conversation statistics using NumPy, and conversation reports using Pandas.| "level4_module4/chatbot_level4.py"

Every level is designed to be a complete, runnable program on its own. Level 4 is the final submitted utility, combining chatbot interaction, conversation management, file handling, object-oriented programming, and data analysis.

3. Installation and Execution

Requirements: Python 3.8 or above.

# Clone the repository
git clone https://github.com/<your-username>/simple-chatbot-python.git

# Open the project folder
cd simple-chatbot-python

# Run Level 1
python level1_module1/chatbot_level1.py

# Run Level 2
python level2_module2/chatbot_level2.py

# Run Level 3
python level3_module3/chatbot_level3.py

# Install libraries required for Level 4
python -m pip install numpy pandas

# Run Level 4
python level4_module4/chatbot_level4.py

Levels 1 to 3 use Python's built-in features and do not require external libraries. Level 4 requires NumPy and Pandas for conversation-data analysis.

4. Summary of the Logic Used

Predefined responses: A Python dictionary stores common greetings, questions, and commands with their corresponding chatbot responses. The chatbot searches for a suitable response based on the user's input.

Input validation: User input is checked before processing. String methods such as "strip()", "lower()", and "split()" help clean and normalize messages. Later levels use exception handling to manage invalid input and unexpected errors.

Control flow: A "while" loop keeps the conversation active until the user chooses to exit. Conditional statements such as "if", "elif", and "else" determine which response should be displayed.

Conversation history: A list stores previous user messages and chatbot responses. Tuples can be used to organize individual conversation entries, while a set records unique user queries.

Modularity: From Level 3, the chatbot is divided into small functions such as "get_response()", "show_menu()", "show_history()", "show_statistics()", and "save_history()". This makes the program easier to read, maintain, reuse, and test.

Object model: Level 4 represents the chatbot and its conversation manager using classes. Inheritance can be used to create specialized chatbot classes, while encapsulation helps manage conversation records and chatbot data.

Persistence: Conversation records are saved to a CSV file so they can be accessed after the program closes. A text report can also be generated using Python's "open()" function and the "with" statement.

Analysis: NumPy can calculate numerical statistics from conversation data, where applicable. Pandas can read saved CSV records and generate reports using functions such as "describe()", "groupby()", and "value_counts()".

User interaction: The chatbot provides options to start a conversation, view available questions, review conversation history, display statistics, save records, and exit the application.

5. Repository Structure

simple-chatbot-python/
├── README.md
├── level1_module1/
│   └── chatbot_level1.py
├── level2_module2/
│   └── chatbot_level2.py
├── level3_module3/
│   └── chatbot_level3.py
├── level4_module4/
│   └── chatbot_level4.py
└── Consolidated_Report.pdf

6. Assessment Mapping

Assessment| Week| Deliverable from this repository
Utility Assessment-I| Week 4| Level 1 chatbot working, repository initialized, first commits completed, and README started.
Utility Assessment-II| Week 8| Levels 2 and 3 completed, data structures and functions implemented, feature branches merged, and meaningful commit history maintained.
Utility Assessment-III| Week 12| Level 4 completed and tested, conversation storage and analysis implemented, README finalized, and final demonstration prepared.
Utility Report| —| "Consolidated_Report.pdf" containing the complete chatbot project report uploaded to the repository.

Final Project: Simple Chatbot Using Python — an interactive, menu-driven chatbot that demonstrates Python fundamentals, data structures, functions, exception handling, file handling, object-oriented programming, and basic data analysis.
