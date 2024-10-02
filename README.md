# Library Management System
## Project Overview
Welcome to the Library Management System! This is a command-line-based Python application designed to streamline the management of books and resources within a library. Users can browse, borrow, return, and explore a collection of books while leveraging a MySQL database for data storage and retrieval.

The project is structured into multiple Python files to ensure clean code organization and maintainability. It includes robust error handling and input validation to provide a smooth user experience.

## Features
* *Book Operations:* Add, borrow, return, search, and display books.
* *User Management:* Add new users, view user details, and display all users.
* *Author Management:* Add new authors, view author details, and display all authors.
* *Database Integration:* Utilizes a MySQL database to store and manage data related to books, users, and authors.
* *User-Friendly CLI:* Simple and intuitive menu-driven interface.
* *Input Validation:* Ensures that user inputs are in the correct format.
* *Error Handling:* Graceful handling of invalid input and database-related errors.
## File Structure
This project is organized across multiple files to improve readability and code management.
Here’s a breakdown of the key files:
```
library-management-system/
├── db/                       # Directory containing database-related scripts.
│   ├── create_tables.py      # Script to create necessary tables in the database.
│   └── database.py           # Functions for creating database connection.
├── models/                   # Directory containing model files.
│   ├── author.py             # Model representing an author.
│   ├── book.py               # Model representing a book.
│   ├── borrowed_book.py      # Model representing borrowed books.
│   └── user.py               # Model representing a user.
├── operations/               # Directory containing operational scripts.
│   ├── author_operations.py   # Functions for managing author-related operations.
│   ├── book_operations.py     # Functions for managing book-related operations.
│   └── user_operations.py     # Functions for managing user-related operations.
├── main.py                   # Main entry point for the application (UI and menu).
├── menu_handler.py           # Handles display of menus and user input.
└── README.md                 # Project overview and instructions.
```
## How to Set Up the Database
1. Clone the Repository:
```
git clone https://github.com/MatthewGUser/CT-MP_SQL.git
cd CT-MP_SQL
```
2. Set Up MySQL:
* Ensure you have MySQL installed on your machine.
* Create a new database for the Library Management System. You can use the MySQL command line or a tool like MySQL Workbench:
```
CREATE DATABASE library_management_system;
USE library_management_system;
```
3. Configure Database Connection:
* Open the `database.py` file and update the connection parameters (host, user, password, and database name) to match your MySQL setup.
4. Create Tables:
* Run the `database.py` file to create the necessary tables in your MySQL database:
```
python database.py
```
## How to Run the Application
1. Run the Application: In your terminal, run the main file to start the program:
```
python main.py
```
2. **Menu Options:** Once the program is running, you’ll be greeted with the following menu:
```
Welcome to the Library Management System!
Menu:
1. Book Operations
2. User Operations
3. Author Operations
4. Quit
```
3. **Follow the Instructions:** Choose the number corresponding to the action you want to take and follow the prompts to manage your library.

4. **Open MySQL Client/Terminal:** Execute the following commands to check information:
```
USE library_management_system;
SHOW TABLES;
SELECT * FROM authors;
SELECT * FROM books;
SELECT * FROM borrowed_books;
SELECT * FROM users;
```
## Example Usage
Here’s a sample interaction with the Library Management System:
```
Welcome to the Library Management System!
Menu:
1. Book Operations
2. User Operations
3. Author Operations
4. Quit

Select an option (1-4): 1
Book Operations:
1. Add a new book
2. Borrow a book
3. Return a book
4. Search for a book
5. Display all books
6. Back to Main Menu
```
## Input Validation
* Input validation ensures that all data entered by the user (e.g., book titles, user IDs) adheres to the expected format.
* Error handling gracefully manages invalid inputs and database-related errors.
## Project Structure
```
library-management-system/
├── main.py                   # Main entry point for the application (UI and menu).
├── models/                   # Contains models for Book, User, Author, BorrowedBook.
│   ├── author.py             
│   ├── book.py              
│   ├── user.py              
│   └── borrowed_book.py      
├── operations/               # Functions for managing book, user, and author operations.
│   ├── author_operations.py   
│   ├── book_operations.py     
│   └── user_operations.py     
├── database.py               # Functions for creating database connection and tables.
├── menu_handler.py           # Handles display of menus and user input.
└── README.md                 # Project overview and instructions.
```
## Conclusion
This Library Management System provides a comprehensive solution for managing library resources, featuring a modular code structure for better organization and maintainability.