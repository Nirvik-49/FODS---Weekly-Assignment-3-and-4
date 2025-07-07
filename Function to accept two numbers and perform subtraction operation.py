def subtract(num1, num2):
    """Function to subtract the second number from the first."""
    return num1 - num2

def main():
    # Input two numbers from the user
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    
    # Call the subtraction function
    result = subtract(number1, number2)
    
    # Display the result
    print(f"The result of subtracting {number2} from {number1} is: {result}")

# Directly call the main function
main()
