# Write a Python function named print diamond that takes an odd integer n as an argument 
# and prints a diamond shape with a width of n using the * character.

# Note: If an even number is passed, the function should return "Please provide an odd integer."


def print_diamond_shape():
    try:

# Prompt user to enter a number
        width = int(input("Enter a number for the diamond's width: "))

# Check if the inputted number is an odd number
        if width % 2 == 0:
            print("Please provide an odd integer.")
            return

# Main
        for i in range (1, width+1, 2):
            print(("*" * i).center(width))

        for i in range (width-2, 0, -2):
            print(("*" * i).center(width))

# Handle non-integer inputs
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Call the function
print_diamond_shape()