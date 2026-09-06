"""
Dice Rolling Simulator
Simulates rolling one or more dice with a chosen number of sides.
"""

import random


def roll_dice(num_dice=1, sides=6):
    return [random.randint(1, sides) for _ in range(num_dice)]


def get_positive_int(prompt, default):
    value = input(prompt).strip()
    if value == "":
        return default
    try:
        num = int(value)
        return num if num > 0 else default
    except ValueError:
        print("Invalid input, using default value.")
        return default


def main():
    print("=== Dice Rolling Simulator ===")

    while True:
        num_dice = get_positive_int("How many dice do you want to roll? (default 1): ", 1)
        sides = get_positive_int("How many sides per die? (default 6): ", 6)

        results = roll_dice(num_dice, sides)
        print(f"\nRolling {num_dice} dice with {sides} sides each...")
        print(f"Results: {results}")
        print(f"Total: {sum(results)}\n")

        again = input("Roll again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
