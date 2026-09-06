"""
Password Strength Checker
Analyzes a password and rates its strength based on length,
character variety, and common weaknesses.
"""

import re

COMMON_PASSWORDS = {
    "password", "123456", "123456789", "qwerty", "abc123",
    "111111", "letmein", "welcome", "admin", "iloveyou",
}


def check_password_strength(password):
    score = 0
    feedback = []

    if password.lower() in COMMON_PASSWORDS:
        return 0, ["This is a very common password. Avoid using it."]

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    if len(password) >= 12:
        score += 1

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add numbers.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add special characters (!@#$%^&* etc.).")

    return score, feedback


def get_strength_label(score):
    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Moderate"
    else:
        return "Strong"


def main():
    print("=== Password Strength Checker ===")

    while True:
        password = input("\nEnter a password to check (or 'exit' to quit): ").strip()
        if password.lower() == "exit":
            print("Goodbye!")
            break

        score, feedback = check_password_strength(password)
        strength = get_strength_label(score)

        print(f"\nStrength: {strength} (Score: {score}/6)")
        if feedback:
            print("Suggestions to improve:")
            for tip in feedback:
                print(f" - {tip}")
        else:
            print("Great job! Your password is strong.")


if __name__ == "__main__":
    main()
