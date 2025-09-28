# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    """Display the current date and time in YYYY-MM-DD HH:MM:SS format."""
    current_date = datetime.now()  # get current date and time
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date(days_to_add):
    """Calculate and display the future date after adding given days."""
    current_date = datetime.now()  # get current date and time
    future_date = current_date + timedelta(days=days_to_add)  # add days
    print("Future date:", future_date.strftime("%Y-%m-%d"))

if __name__ == "__main__":
    # Part 1: Display the current date and time
    display_current_datetime()

    # Part 2: Ask for days to add and show future date
    days = int(input("Enter the number of days to add to the current date: "))
    calculate_future_date(days)
