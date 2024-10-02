def display_main_menu():
    """Displays the main menu options for the Library Management System."""
    print("Welcome to the Library Management System with Database Integration!")
    print("****")
    print("Main Menu:")
    print("1. Book Operations")
    print("2. User Operations")
    print("3. Author Operations")
    print("4. Quit")
    print("****")


def display_book_operations():
    """Displays the book operation menu options."""
    print("Book Operations:")
    print("1. Add a new book")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Search for a book")
    print("5. Display all books")
    print("6. Back to Main Menu")
    print("****")


def display_user_operations():
    """Displays the user operation menu options."""
    print("User Operations:")
    print("1. Add a new user")
    print("2. View user details")
    print("3. Display all users")
    print("4. Back to Main Menu")
    print("****")


def display_author_operations():
    """Displays the author operation menu options."""
    print("Author Operations:")
    print("1. Add a new author")
    print("2. View author details")
    print("3. Display all authors")
    print("4. Back to Main Menu")
    print("****")


def get_user_choice(menu_type):
    """Gets the user's choice based on the menu type."""
    choice = input(f"Please enter your choice for {menu_type}: ")
    return choice


def display_invalid_choice():
    """Displays a message for an invalid menu choice."""
    print("Invalid choice, please try again.")
    print("****")


