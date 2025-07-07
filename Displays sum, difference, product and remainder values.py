def calculate_operations(num1, num2):
    # Calculate sum
    sum_value = num1 + num2
    
    # Calculate difference
    difference_value = num1 - num2
    
    # Calculate product
    product_value = num1 * num2
    
    # Calculate remainder
    remainder_value = num1 % num2

    # Display the results
    print(f"Sum: {sum_value}")
    print(f"Difference: {difference_value}")
    print(f"Product: {product_value}")
    print(f"Remainder: {remainder_value}")


if __name__ == "__main__":
    # Input two numbers
    
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    
    # Call the function
    calculate_operations(number1, number2)
