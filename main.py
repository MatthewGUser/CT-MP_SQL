from db.create_tables import create_tables  # Import the create_tables function
from models.author import Author
from models.user import User
from models.borrowed_book import BorrowedBook
from operations.book_operations import (
    add_book,
    search_book,
    borrow_book,
    return_book,
    display_books
)
from operations.user_operations import (
    add_user,
    view_user_details,
    display_all_users
)
from operations.author_operations import (
    add_author,
    view_author_details,
    display_all_authors
)
from datetime import datetime
from menu_handler import (
    display_main_menu,
    display_book_operations,
    display_user_operations,
    display_author_operations,
    get_user_choice,
    display_invalid_choice,
)

def main():
    # Create tables if they do not exist
    create_tables()
    
    main_menu()  # Start the main menu loop

def main_menu():
    while True:
        display_main_menu()
        choice = get_user_choice("main")

        if choice == '1':
            book_operations()
        elif choice == '2':
            user_operations()
        elif choice == '3':
            author_operations()
        elif choice == '4':
            print("Thank you for using the Library Management System!")
            break
        else:
            display_invalid_choice()

def book_operations():
    while True:
        display_book_operations()
        choice = get_user_choice("book")

        if choice == '1':
            title = input("Enter book title: ")
            author_id = input("Enter author ID: ")
            isbn = input("Enter ISBN: ")
            publication_date = input("Enter publication date (YYYY-MM-DD): ")

            # Validate date format
            try:
                datetime.strptime(publication_date, '%Y-%m-%d')
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
                continue

            add_book(title, author_id, isbn, publication_date)
        elif choice == '2':
            user_id = input("Enter your user ID: ")
            book_id = input("Enter book ID to borrow: ")
            borrow_book(user_id, book_id)
        elif choice == '3':
            user_id = input("Enter your user ID: ")
            book_id = input("Enter book ID to return: ")
            return_book(user_id, book_id)
        elif choice == '4':
            title = input("Enter book title to search: ")
            results = search_book(title)
            if results:
                for book in results:
                    print(book)
            else:
                print("No books found.")
        elif choice == '5':
            display_books()
        elif choice == '6':
            break
        else:
            display_invalid_choice()

def user_operations():
    while True:
        display_user_operations()
        choice = get_user_choice("user")

        if choice == '1':
            name = input("Enter user name: ")
            library_id = input("Enter library ID: ")
            add_user(name, library_id)
        elif choice == '2':
            user_id = input("Enter user ID to view: ")
            user_details = view_user_details(user_id)
            if user_details:
                print(user_details)
            else:
                print("User not found.")
        elif choice == '3':
            display_all_users()
        elif choice == '4':
            break
        else:
            display_invalid_choice()

def author_operations():
    while True:
        display_author_operations()
        choice = get_user_choice("author")

        if choice == '1':
            name = input("Enter author name: ")
            biography = input("Enter author biography: ")
            add_author(name, biography)
        elif choice == '2':
            author_id = input("Enter author ID to view: ")
            author_details = view_author_details(author_id)
            if author_details:
                print(author_details)
            else:
                print("Author not found.")
        elif choice == '3':
            display_all_authors()
        elif choice == '4':
            break
        else:
            display_invalid_choice()

if __name__ == "__main__":
    main()
