def floor_divide(num1, num2):
    """
    Function to perform floor division of num1 by num2.
    Returns the largest integer less than or equal to the quotient.
    """
    
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    return num1 // num2

def get_numbers():
    """Input two numbers from the user."""
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    return num1, num2

def main():
    # Get input from user
    num1, num2 = get_numbers()
    
    # Perform floor division
    result = floor_divide(num1, num2)
    
    # Display the result
    print(f"The floor division of {num1} by {num2} is: {result}")

# Execute the program
main()
