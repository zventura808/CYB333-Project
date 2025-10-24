# Automated Password Strength Checker

**Author:** Zacchary Ventura  
**Course:** CYB 333 – Security Automation  
**Date:** [10/23/2025]  

---

## 1. Project Overview
The Automated Password Strength Checker is a Python-based tool that evaluates the strength of a user’s password and provides feedback on how to improve it. The goal of this project is to automate password security checks, helping users create stronger and safer passwords.  

The program evaluates passwords based on:  
- Length  
- Character variety (uppercase, lowercase, numbers, special characters)  
- Common weak patterns (like “1234”, “password”, or repeated characters)  

Once evaluated, the password is rated as **Weak**, **Medium**, or **Strong**, and suggestions are provided for improvement. This project demonstrates how automation can improve security practices and reduce human error.

---

## 2. Key Features
1. **Automated Evaluation:** Quickly checks password strength and provides a rating.  
2. **Improvement Suggestions:** Gives actionable tips to strengthen weak passwords.  
3. **Pattern Detection:** Flags common weak passwords and predictable sequences.  
4. **CLI Interface:** Users can enter passwords directly in the terminal.  
5. **Lightweight:** Only requires Python 3.x and built-in libraries.  

---

## 3. Setup and Usage

### 3.1 Clone the Repository
```bash
git clone https://github.com/zventura808/CYB333-Project.git
cd CYB333-Project

python -m venv venv
venv\Scripts\activate

python password_checker.py

5. Code Documentation

check_password_strength(password): Evaluates password length, character types, and weak patterns. Returns a score, rating, and suggestions.

contains_common_patterns(password): Detects simple patterns and common weak passwords.

display_results(password): Shows the rating and improvement tips to the user.

main(): Entry point of the script; prompts user for input and displays results.

All functions are clearly commented and use meaningful names. The code follows Python formatting standards (PEP 8).

6. Future Enhancements

Add a database of leaked passwords for breach checks.

Implement a GUI interface for easier use.

Create a more advanced scoring system based on password entropy.

Allow batch password checking from a file.
