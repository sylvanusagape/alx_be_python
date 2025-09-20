# pattern_drawing.py
# This program draws a square pattern of asterisks based on user input.

# Prompt the user for the pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter for the while loop
row = 0

# While loop for each row
while row < size:
    # For loop for printing asterisks in each row
    for col in range(size):
        print("*", end="")  # print * without moving to next line
    print()  # move to the next line after each row
    row += 1  # increment row counter
