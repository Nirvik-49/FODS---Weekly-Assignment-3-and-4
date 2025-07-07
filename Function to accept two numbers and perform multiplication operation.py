def multiply(num1, num2):
    """Function to multiply two numbers."""
    return num1 * num2

def main():
    # Input two numbers from the user
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    
    # Call the multiplication function
    result = multiply(number1, number2)
    
    # Display the result
    print(f"The product of {number1} and {number2} is: {result}")

# Directly call the main function
main()
