def segregate_numbers():
    """Segregate continuous user input into even and odd lists"""
    
    even_numbers = []
    odd_numbers = []
    
    print("Enter numbers one by one. Type 'exit' to finish.")
    
    while True:
        user_input = input("Enter a number (or 'exit' to finish): ")
        
        # Check if user wants to exit
        
        if user_input.lower() == 'exit':
            break
        
        # Validate input is a number
        try:
            number = float(user_input)
            # Check if it's an integer (even/odd applies to whole numbers)
            if number.is_integer():
                number = int(number)
                if number % 2 == 0:
                    even_numbers.append(number)
                else:
                    odd_numbers.append(number)
            else:
                print("Please enter whole numbers (decimals will be ignored)")
        except ValueError:
            print("Invalid input. Please enter a number or 'exit'.")
    
    # Display results
    print("\nResults:")
    print("-" * 50)
    print(f"Even numbers: {even_numbers}")
    print(f"Count: {len(even_numbers)}")
    print("-" * 50)
    print(f"Odd numbers: {odd_numbers}")
    print(f"Count: {len(odd_numbers)}")
    print("-" * 50)

if __name__ == "__main__":
    segregate_numbers()
