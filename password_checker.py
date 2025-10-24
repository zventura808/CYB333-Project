"""
Automated Password Strength Checker
Author: Zacchary Ventura
Course: CYB 333 - Security Automation
Description:
    This script evaluates the strength of a user's password and provides
    feedback on how to make it stronger. It checks for length, character
    variety, and common weak patterns.
"""

import re
import string


def check_password_strength(password):
    """
    Evaluates the strength of the given password based on length,
    character diversity, and common patterns.
    Returns a tuple (score, rating, suggestions)
    """
    score = 0
    suggestions = []

    # Check password length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters for better security.")

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add lowercase letters.")

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letters.")

    # Check for numbers
    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append("Include some numbers.")

    # Check for special characters
    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        suggestions.append("Add special characters like !, @, or #.")

    # Check for common weak patterns
    if contains_common_patterns(password):
        score -= 2
        suggestions.append("Avoid common passwords or simple patterns like '1234' or 'password'.")

    # Determine password rating
    if score >= 6:
        rating = "STRONG"
    elif 3 <= score < 6:
        rating = "MEDIUM"
    else:
        rating = "WEAK"

    return score, rating, suggestions


def contains_common_patterns(password):
    """
    Checks if the password contains weak or predictable patterns.
    Returns True if any weak pattern is found.
    """
    common_patterns = [
        "password", "1234", "qwerty", "admin", "letmein", "welcome", "abc123"
    ]
    for pattern in common_patterns:
        if pattern.lower() in password.lower():
            return True
    return False


def display_results(password):
    """
    Displays the results of the password strength check.
    """
    score, rating, suggestions = check_password_strength(password)
    print("\nPassword Strength:", rating)

    if suggestions:
        print("Tips:")
        for tip in suggestions:
            print("-", tip)
    else:
        print("Great job! Your password looks strong.")


def main():
    """
    Main function that runs the password checker.
    """
    print("====================================")
    print(" Automated Password Strength Checker")
    print("====================================")
    user_password = input("Enter a password to check: ")

    display_results(user_password)
    print("\nDone! Always remember to use unique, strong passwords for every account.")


# Run the program
if __name__ == "__main__":
    main()
