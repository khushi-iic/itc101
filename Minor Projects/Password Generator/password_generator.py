"""
Password Generator
Generates a random, secure password based on user-specified criteria.
"""

import random
import string


def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True):
    if length < 4:
        raise ValueError("Password length should be at least 4 for good security.")

    pool = list(string.ascii_lowercase)
    guaranteed = [random.choice(string.ascii_lowercase)]

    if use_upper:
        pool += list(string.ascii_uppercase)
        guaranteed.append(random.choice(string.ascii_uppercase))
    if use_digits:
        pool += list(string.digits)
        guaranteed.append(random.choice(string.digits))
    if use_symbols:
        pool += list(string.punctuation)
        guaranteed.append(random.choice(string.punctuation))

    remaining_length = length - len(guaranteed)
    password_chars = guaranteed + [random.choice(pool) for _ in range(remaining_length)]
    random.shuffle(password_chars)

    return "".join(password_chars)


def get_yes_no(prompt):
    while True:
        choice = input(prompt).strip().lower()
        if choice in ("y", "yes"):
            return True
        if choice in ("n", "no"):
            return False
        print("Please answer 'y' or 'n'.")


def main():
    print("=== Password Generator ===")

    while True:
        try:
            length = int(input("Enter desired password length (min 4): "))
            if length < 4:
                print("Length must be at least 4.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    use_upper = get_yes_no("Include uppercase letters? (y/n): ")
    use_digits = get_yes_no("Include digits? (y/n): ")
    use_symbols = get_yes_no("Include symbols? (y/n): ")

    password = generate_password(length, use_upper, use_digits, use_symbols)
    print(f"\nGenerated Password: {password}")


if __name__ == "__main__":
    main()
