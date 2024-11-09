"""
Question 1: Library Management System (10 marks)
Scenario: You are building a basic library management system to track books and
borrowers.
"""
# A Class To Represent the Book Entity
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def mark_as_borrowed(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f'Book "{self.title} has been borrowed.')
        else:
            print(f'Book "{self.title}" is already borrowed.')

    def mark_as_returned(self):
        if self.is_borrowed:
            self.is_borrowed = False 
            print(f'Book "{self.title}" has been returned.')
        else:
            print(f'Book "{self.title}" was not borrowed.')


# Class for a Library Member
class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.is_borrowed:
            print(f'Sorry, "{book.title}" is currently borrowed by someone else.')
        else:
            book.mark_as_borrowed()
            self.borrowed_books.append(book)
            print(f'{self.name} has borrowed "{book.title}".')

    def return_book(self, book):
        if book in self.borrow_books:
            book.mark_as_returned()
            self.borrowed_books.remove(book)
            print(f'{self.name} has returned "{book.title}".')
        else:
            print(f'{self.name} did not borrow "{book.title}".')

    def list_borrowed_books(self):
        if self.borrowed_books:
            print(f'{self.name} has borrowed the following books:')
            for book in self.borrowed_books:
                print(f'- {book.title} by {book.author}')
        else:
            print(f'{self.name} has not borrowed any books.')


# Interactive Code
def main():
    # Create some sample books
    book1 = Book("1984", "George Orwell")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")
    book3 = Book("The Great Gasby", "F. Scott Fitzergerald")

    # Create a library member
    member = LibraryMember("Alice", "M001")

    # Interactive Menu
    while True:
        print("\nLibrary Menu:")
        print("1. Borrow a Book")
        print("2. Return a Book")
        print("3. List Borrowed Books")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nAvailable Books:")
            available_books = [book for book in [book1, book2, book3] if not book.is_borrowed]
            if available_books:
                for i, book in enumerate(available_books, start=1):
                    print(f"{i}. {book.title} by {book.author}")
                book_choice = int(input("Enter the book number you want to borrow: ")) - 1
                if 0 <= book_choice < len(available_books):
                    member.borrow_book(available_books[book_choice])
                else:
                    print("Invalid choice.")
            else:
                print("No books are available to borrow")

        elif choice == "2":
            print("\nBooks You Have Borrowed:")
            if member.borrowed_books:
                for i, book in enumerate(member.borrowed_books, start=1):
                    print(f"{i}. {book.title} by {book.author}")
                book_choice = int(input("Enter the book number you want to return: "))
                if 0 <= book_choice < len(member.borrowed_books):
                    member.return_book(member.borrowed_books[book_choice])
                else:
                    print("Invalid choice.")
            else:
                print("You have no books to return.")

        elif choice == "3":
            member.list_borrowed_books()

        elif choice == "4":
            print("Exiting the library system. Goodbye!")
            break 

        else:
            print("Invalid choice. Please try again.")

# Run the interactive code
main()