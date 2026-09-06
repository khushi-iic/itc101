"""
Simple Calculator
A basic command-line calculator supporting +, -, *, /, and % operations.
"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b


def modulus(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a % b


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def main():
    print("=== Simple Calculator ===")
    print("Operations: + (add), - (subtract), * (multiply), / (divide), % (modulus)")
    print("Type 'exit' to quit.\n")

    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
        "%": modulus,
    }

    while True:
        op = input("Enter operation (+, -, *, /, %) or 'exit': ").strip()
        if op.lower() == "exit":
            print("Goodbye!")
            break
        if op not in operations:
            print("Invalid operation. Try again.\n")
            continue

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        result = operations[op](num1, num2)
        print(f"Result: {result}\n")


if __name__ == "__main__":
    main()
