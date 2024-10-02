from db.database import get_connection
from datetime import datetime

def add_book(title, author_id, isbn, publication_date):
    """Add a new book to the database."""
    connection = get_connection()
    cursor = connection.cursor()
    
    try:
        query = """
        INSERT INTO books (title, author_id, isbn, publication_date, availability)
        VALUES (%s, %s, %s, %s, TRUE)
        """
        cursor.execute(query, (title, author_id, isbn, publication_date))
        connection.commit()
        print("Book added successfully.")
    except Exception as e:
        print(f"Error adding book: {e}")
    finally:
        cursor.close()
        connection.close()

def search_book(title):
    """Search for a book by title."""
    connection = get_connection()
    cursor = connection.cursor()
    
    try:
        query = "SELECT * FROM books WHERE title LIKE %s"
        cursor.execute(query, (f"%{title}%",))
        results = cursor.fetchall()
        return results
    except Exception as e:
        print(f"Error searching for book: {e}")
    finally:
        cursor.close()
        connection.close()

def borrow_book(user_id, book_id):
    """Borrow a book by updating its availability and recording the transaction."""
    connection = get_connection()
    cursor = connection.cursor()
    
    try:
        query = "UPDATE books SET availability = FALSE WHERE id = %s"
        cursor.execute(query, (book_id,))
        
        borrow_query = """
        INSERT INTO borrowed_books (user_id, book_id, borrow_date)
        VALUES (%s, %s, %s)
        """
        cursor.execute(borrow_query, (user_id, book_id, datetime.now()))
        
        connection.commit()
        print("Book borrowed successfully.")
    except Exception as e:
        print(f"Error borrowing book: {e}")
    finally:
        cursor.close()
        connection.close()

def return_book(user_id, book_id):
    """Return a borrowed book and update its availability."""
    connection = get_connection()
    cursor = connection.cursor()
    
    try:
        query = "UPDATE books SET availability = TRUE WHERE id = %s"
        cursor.execute(query, (book_id,))
        
        return_query = "DELETE FROM borrowed_books WHERE user_id = %s AND book_id = %s"
        cursor.execute(return_query, (user_id, book_id))
        
        connection.commit()
        print("Book returned successfully.")
    except Exception as e:
        print(f"Error returning book: {e}")
    finally:
        cursor.close()
        connection.close()

def display_books():
    """Display all books in the database."""
    connection = get_connection()
    cursor = connection.cursor()
    
    try:
        query = "SELECT * FROM books"
        cursor.execute(query)
        results = cursor.fetchall()
        
        print("List of Books:")
        for book in results:
            print(book)
    except Exception as e:
        print(f"Error displaying books: {e}")
    finally:
        cursor.close()
        connection.close()
