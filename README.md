# Automated Password Strength Checker

**Author:** Zacchary Ventura  
**Course:** CYB 333 – Security Automation  
**Date:** [10/23/2025]  

---

## Project Overview
The Automated Password Strength Checker is a Python-based tool that evaluates the strength of a user’s password and provides feedback on how to improve it. The goal of this project is to automate password security checks, helping users create stronger and safer passwords.  

The program evaluates passwords based on:  
- Length  
- Character variety (uppercase, lowercase, numbers, special characters)  
- Common weak patterns (like “1234”, “password”, or repeated characters)  

Once evaluated, the password is rated as **Weak**, **Medium**, or **Strong**, and suggestions are provided for improvement. This project demonstrates how automation can improve security practices and reduce human error.

---

## Key Features
- **Automated Evaluation:** Quickly checks password strength and provides a rating.  
- **Improvement Suggestions:** Gives actionable tips to strengthen weak passwords.  
- **Pattern Detection:** Flags common weak passwords and predictable sequences.  
- **CLI Interface:** Users can enter passwords directly in the terminal.  
- **Lightweight:** Only requires Python 3.x and built-in libraries.  

---

## Setup and Usage

### 1. Clone the Repository
```bash
git clone https://github.com/zventura808/CYB333-Project.git
cd CYB333-Project

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

```bash
python password_checker.py

Example output:
Enter a password: myPassword123

Password Strength: MEDIUM
Tips:
- Add special characters like !, @, or #
