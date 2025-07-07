def modulo(num1, num2):
    """Function to perform modulo division of the first number by the second."""

    if num2 == 0:
        return "Error: Division by zero is not allowed."
    return num1 % num2

def main():
    # Input two numbers from the user
    
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    
    # Call the modulo function
    result = modulo(number1, number2)
    
    # Display the result
    print(f"The result of {number1} modulo {number2} is: {result}")

# Directly call the main function
main()
