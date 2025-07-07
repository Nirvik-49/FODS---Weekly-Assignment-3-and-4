def word_frequency(sentence):
    """Return a dictionary containing the frequency of each word in the sentence."""
    
    # Split the sentence into words
    words = sentence.split()
    
    # Initialize an empty dictionary to store word frequencies
    frequency = {}
    
    # Iterate through each word in the list of words
    for word in words:

        # Convert word to lowercase to ensure case-insensitivity
        word = word.lower()
        
        # Update the frequency count for the word
        
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
            
    return frequency

# Test the function
if __name__ == "__main__":
    # Example sentence
    test_sentence = "This is a test. This test is only a test."
    
    # Get the word frequency
    result = word_frequency(test_sentence)
    
    # Display the result
    print("Word Frequency:", result)
