# CYB333-Project
The Automated Password Strength Checker is a Python-based tool that evaluates the strength of a password and provides feedback on how to improve it. The goal of this project is to automate the process of checking password quality, which is a common but repetitive task in cybersecurity.

The program evaluates passwords based on:

Length

Character variety (uppercase, lowercase, numbers, special characters)

Common weak patterns (like “1234”, “password”, or repeated characters)

Once evaluated, the password is rated as Weak, Medium, or Strong, and suggestions are provided to improve weak passwords. This project demonstrates how automation can improve security practices by reducing human error and saving time.

Key Features

Automated Password Evaluation: Quickly checks password strength and outputs a rating.

Improvement Suggestions: Gives actionable tips to make weak passwords stronger.

Pattern Detection: Flags common weak passwords and predictable sequences.

Simple CLI Interface: Users can enter passwords directly in the terminal.

Lightweight: Only requires Python 3.x and built-in libraries.

Setup and Usage
1. Clone the Repository
git clone https://github.com/zventura808/CYB333-Project.git
cd CYB333-Project

2. Install Dependencies

No external libraries are required. The script uses Python’s built-in re and string modules. Make sure you have Python 3.8+ installed.

Optional: Create a virtual environment:

python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

3. Run the Script
python password_checker.py


Enter your password when prompted. The script will display a strength rating and improvement suggestions.

Example Output
Enter a password: myPassword123

Password Strength: MEDIUM
Tips:
- Add special characters like !, @, or #

Enter a password: Myp@ssword123!

Password Strength: STRONG
Tips:
- Great job! Your password has a good mix of characters and is long enough.

Dependencies

Python 3.8 or higher

Built-in libraries: re, string, sys

Code Documentation

check_password_strength(password): Evaluates password length, character types, and weak patterns. Returns a score, rating, and suggestions.

contains_common_patterns(password): Detects simple patterns and common weak passwords.

display_results(password): Displays rating and improvement tips to the user.

main(): Entry point of the script; prompts user for input and calls the results display.

All functions are clearly commented, use meaningful names, and follow consistent Python formatting (PEP 8).

Additional Notes

This project was created for the CYB 333 Security Automation course. Possible future improvements include:

Adding a database of leaked passwords for breach checks

Implementing a GUI interface

Creating a scoring system based on entropy
