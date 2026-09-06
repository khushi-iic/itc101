"""
Word Counter
Counts words, characters, sentences, and word frequency in a given text.
Supports direct text input or reading from a .txt file.
"""

import re
from collections import Counter


def count_words(text):
    words = re.findall(r"\b\w+\b", text)
    return len(words)


def count_characters(text, include_spaces=True):
    if include_spaces:
        return len(text)
    return len(text.replace(" ", ""))


def count_sentences(text):
    sentences = re.split(r"[.!?]+", text)
    sentences = [s for s in sentences if s.strip()]
    return len(sentences)


def word_frequency(text, top_n=10):
    words = re.findall(r"\b\w+\b", text.lower())
    counter = Counter(words)
    return counter.most_common(top_n)


def analyze_text(text):
    print("\n=== Text Analysis ===")
    print(f"Word count: {count_words(text)}")
    print(f"Character count (with spaces): {count_characters(text, True)}")
    print(f"Character count (without spaces): {count_characters(text, False)}")
    print(f"Sentence count: {count_sentences(text)}")

    print("\nTop 10 most frequent words:")
    for word, freq in word_frequency(text):
        print(f"  {word}: {freq}")


def get_text_from_file(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None


def main():
    print("=== Word Counter ===")
    print("1. Enter text manually")
    print("2. Load text from a .txt file")

    choice = input("\nChoose an option (1 or 2): ").strip()

    text = None
    if choice == "1":
        text = input("\nEnter your text:\n")
    elif choice == "2":
        filepath = input("Enter the path to the .txt file: ").strip()
        text = get_text_from_file(filepath)
    else:
        print("Invalid choice.")
        return

    if text and text.strip():
        analyze_text(text)
    else:
        print("No text to analyze.")


if __name__ == "__main__":
    main()
