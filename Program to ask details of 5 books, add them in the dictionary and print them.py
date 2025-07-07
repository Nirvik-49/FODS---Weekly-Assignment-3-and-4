def get_book_details():
    """Collect details of 5 books from the user"""
    books = {}
    
    for i in range(1, 6):
        print(f"\nEnter details for Book {i}:")
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        isbn = input("Enter ISBN: ")
        cost = float(input("Enter cost: "))
        
        books[i] = {
            'title': title,
            'author': author,
            'ISBN': isbn,
            'cost': cost
        }
    
    return books

def print_books(books):
    """Print all book details"""
    print("\nBook Details:")
    print("-" * 50)
    print(f"{'S.No':<5}{'Title':<20}{'Author':<20}{'ISBN':<15}{'Cost':>10}")
    print("-" * 50)
    
    for num, details in books.items():
        print(f"{num:<5}{details['title']:<20}{details['author']:<20}"
              f"{details['ISBN']:<15}${details['cost']:>9.2f}")

if __name__ == "__main__":
    # Get book details from user
    book_collection = get_book_details()
    
    # Print all book details
    print_books(book_collection)
