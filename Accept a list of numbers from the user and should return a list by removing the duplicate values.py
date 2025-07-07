def remove_duplicates(numbers):
    
    """Return a list with duplicate values removed."""
    return list(set(numbers))

# Main program
if __name__ == "__main__":
    
    # Accept a list of numbers from the user
    user_input = input("Enter a list of numbers separated by spaces: ")
    
    # Convert the input string into a list of numbers
    number_list = [int(num) for num in user_input.split()]
    
    # Remove duplicates
    unique_numbers = remove_duplicates(number_list)
    
    # Display the result
    print("List after removing duplicates:", unique_numbers)

