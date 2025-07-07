def divide(num1, num2):
    """Function to divide the first number by the second."""
    
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    return num1 / num2

def main():
    # Input two numbers from the user
    
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    
    # Call the division function
    
    result = divide(number1, number2)
    
    # Display the result
    
    print(f"The result of dividing {number1} by {number2} is: {result}")

# Directly call the main function
main()
