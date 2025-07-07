def count_occurrences(numbers):
    """Count and print the occurrences of each number in the list."""
    
    occurrences = {}
    
    for number in numbers:
        if number in occurrences:
            occurrences[number] += 1
        else:
            occurrences[number] = 1
    
    # Print the occurrences in a formatted way
    
    for number, count in occurrences.items():
        print(f"Number {number} occurs {count} time(s).")

# Test cases
if __name__ == "__main__":
    # Test case 1
    test_list_1 = [1, 2, 2, 3, 4, 4, 4, 5]
    print("Test Case 1:")
    count_occurrences(test_list_1)
    print()

    # Test case 2
    test_list_2 = [10, 20, 10, 30, 20, 10]
    print("Test Case 2:")
    count_occurrences(test_list_2)
    print()

    # Test case 3
    test_list_3 = [5, 5, 5, 5, 5]
    print("Test Case 3:")
    count_occurrences(test_list_3)
    print()

    # Test case 4
    test_list_4 = []
    print("Test Case 4:")
    count_occurrences(test_list_4)
    print()

    # Test case 5
    test_list_5 = [1, 2, 3, 4, 5, 1, 2, 1]
    print("Test Case 5:")
    count_occurrences(test_list_5)
