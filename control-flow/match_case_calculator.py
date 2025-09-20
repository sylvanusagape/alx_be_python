# match_case_calculator.py
# A simple calculator using Python's match-case statement.

# Prompt for user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

# Perform the calculation using match-case
match operation:
    case "+":  # Addition
        result = num1 + num2
        print(f"The result is {result}.")
    case "-":  # Subtraction
        result = num1 - num2
        print(f"The result is {result}.")
    case "*":  # Multiplication
        result = num1 * num2
        print(f"The result is {result}.")
    case "/":  # Division
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result is {result}.")
    case _:  # Default case for invalid operation
        print("Invalid operation selected.")
