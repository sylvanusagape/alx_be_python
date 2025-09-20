# multiplication_table.py
# This program prints the multiplication table for a given number from 1 to 10.

# Prompt the user for a number
number = int(input("Enter a number to see its multiplication table: "))

# Generate and print the multiplication table using a for loop
for i in range(1, 11):  # loop from 1 to 10 inclusive
    product = number * i
    print(f"{number} * {i} = {product}")
