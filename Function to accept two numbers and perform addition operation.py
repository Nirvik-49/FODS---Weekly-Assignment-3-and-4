def add(num1, num2):
    """Function to add two numbers."""
    
    return num1 + num2

def main():
    # Input two numbers from the user
    
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    
    # Call the addition function
    result = add(number1, number2)
    
    # Display the result
    print(f"The sum of {number1} and {number2} is: {result}")

# Directly call the main function
main()


