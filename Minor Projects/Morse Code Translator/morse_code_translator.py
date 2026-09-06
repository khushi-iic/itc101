"""
Morse Code Translator
Converts text to Morse code and Morse code back to text.
"""

MORSE_CODE_DICT = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
    "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
    "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
    "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
    "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--",
    "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----.",
    ".": ".-.-.-", ",": "--..--", "?": "..--..", "'": ".----.",
    "!": "-.-.--", "/": "-..-.", "(": "-.--.", ")": "-.--.-",
    "&": ".-...", ":": "---...", ";": "-.-.-.", "=": "-...-",
    "+": ".-.-.", "-": "-....-", "_": "..--.-", "\"": ".-..-.",
    "$": "...-..-", "@": ".--.-.", " ": "/",
}

# Reverse dictionary for Morse-to-text conversion
TEXT_CODE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}


def text_to_morse(text):
    text = text.upper()
    morse_words = []

    for char in text:
        if char in MORSE_CODE_DICT:
            morse_words.append(MORSE_CODE_DICT[char])
        else:
            morse_words.append("?")  # Unknown character

    return " ".join(morse_words)


def morse_to_text(morse_code):
    morse_letters = morse_code.strip().split(" ")
    decoded_chars = []

    for code in morse_letters:
        if code == "/":
            decoded_chars.append(" ")
        elif code in TEXT_CODE_DICT:
            decoded_chars.append(TEXT_CODE_DICT[code])
        elif code == "":
            continue
        else:
            decoded_chars.append("?")  # Unknown code

    return "".join(decoded_chars)


def main():
    print("=== Morse Code Translator ===")
    print("1. Text to Morse Code")
    print("2. Morse Code to Text")
    print("Type 'exit' to quit.\n")

    while True:
        choice = input("Choose an option (1/2) or 'exit': ").strip()

        if choice.lower() == "exit":
            print("Goodbye!")
            break

        if choice == "1":
            text = input("Enter text to convert: ").strip()
            if text:
                result = text_to_morse(text)
                print(f"Morse Code: {result}\n")
            else:
                print("Please enter some text.\n")

        elif choice == "2":
            print("Note: Separate letters with spaces, and words with ' / '")
            morse_input = input("Enter Morse code to convert: ").strip()
            if morse_input:
                result = morse_to_text(morse_input)
                print(f"Decoded Text: {result}\n")
            else:
                print("Please enter some Morse code.\n")

        else:
            print("Invalid choice. Please select 1, 2, or 'exit'.\n")


if __name__ == "__main__":
    main()
