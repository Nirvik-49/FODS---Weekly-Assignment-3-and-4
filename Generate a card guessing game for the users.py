import random

def generate_card():
    """Generate a random card with a value and suit."""
    
    card_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    card_suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    
    value = random.choice(card_values)
    suit = random.choice(card_suits)
    
    return value, suit

def get_user_guess():
    """Get the user's guess for the card value and suit."""
    value_guess = input("Guess the card value (2-10, Jack, Queen, King, Ace): ")
    suit_guess = input("Guess the card suit (Hearts, Diamonds, Clubs, Spades): ")
    
    return value_guess, suit_guess

def check_guess(answer, guess):
    
    """Check the user's guess against the answer."""
    
    value_answer, suit_answer = answer
    value_guess, suit_guess = guess
    
    if value_guess == value_answer and suit_guess == suit_answer:
        return "both"  # Both value and suit match
    elif value_guess == value_answer or suit_guess == suit_answer:
        return "one"  # Either value or suit matches
    else:
        return "none"  # Neither matches

def display_result(result):
    
    """Display the result based on the user's guess."""
    
    if result == "both":
        print("❤️😊 Congratulations! You guessed the card correctly!")
    elif result == "one":
        print("😊 You guessed one part correctly!")
    else:
        print("💔 Game Over! Better luck next time!")

def play_game():
    """Main function to play the card guessing game."""
    
    print("Welcome to the Card Guessing Game!")
    
    # Generate a random card
    answer = generate_card()
    print("A card has been drawn. Can you guess it?")
    
    # Get user's guess
    guess = get_user_guess()
    
    # Check the guess
    result = check_guess(answer, guess)
    
    # Display the result
    display_result(result)

if __name__ == "__main__":
    play_game()
