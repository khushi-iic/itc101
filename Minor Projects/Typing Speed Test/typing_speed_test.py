"""
Typing Speed Test
Measures a user's typing speed in Words Per Minute (WPM) and accuracy.
"""

import random
import time

SAMPLE_TEXTS = [
    "The quick brown fox jumps over the lazy dog.",
    "Programming is the art of telling a computer what to do.",
    "Practice makes a person perfect in every field of life.",
    "Python is a versatile and beginner friendly language.",
    "Consistency and discipline are the keys to success.",
]


def calculate_wpm(text, time_taken):
    words = len(text.split())
    minutes = time_taken / 60
    if minutes == 0:
        return 0
    return round(words / minutes, 2)


def calculate_accuracy(original, typed):
    original_words = original.split()
    typed_words = typed.split()

    correct = sum(
        1 for o, t in zip(original_words, typed_words) if o == t
    )
    total = len(original_words)
    if total == 0:
        return 0
    return round((correct / total) * 100, 2)


def main():
    print("=== Typing Speed Test ===")
    sample_text = random.choice(SAMPLE_TEXTS)

    print("\nType the following text as quickly and accurately as you can:")
    print(f"\n\"{sample_text}\"\n")
    input("Press Enter when you're ready to start...")

    start_time = time.time()
    typed_text = input("\nStart typing:\n")
    end_time = time.time()

    time_taken = end_time - start_time
    wpm = calculate_wpm(sample_text, time_taken)
    accuracy = calculate_accuracy(sample_text, typed_text)

    print("\n=== Results ===")
    print(f"Time taken: {time_taken:.2f} seconds")
    print(f"Speed: {wpm} WPM")
    print(f"Accuracy: {accuracy}%")


if __name__ == "__main__":
    main()
