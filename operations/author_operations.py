from db.database import get_connection
from models.author import Author

def add_author(name, biography):
    """Add a new author to the database."""
    connection = get_connection()
    cursor = connection.cursor()
    
    try:
        query = """
        INSERT INTO authors (name, biography)
        VALUES (%s, %s)
        """
        cursor.execute(query, (name, biography))
        connection.commit()
        print("Author added successfully.")
    except Exception as e:
        print(f"Error adding author: {e}")
    finally:
        cursor.close()
        connection.close()


def view_author_details(author_id):
    """View details of a specific author by ID."""
    connection = get_connection()
    cursor = connection.cursor()
    
    try:
        query = "SELECT * FROM authors WHERE id = %s"
        cursor.execute(query, (author_id,))
        result = cursor.fetchone()
        return result
    except Exception as e:
        print(f"Error fetching author details: {e}")
    finally:
        cursor.close()
        connection.close()


def display_all_authors():
    """Display all authors in the database."""
    connection = get_connection()
    cursor = connection.cursor()
    
    try:
        query = "SELECT * FROM authors"
        cursor.execute(query)
        results = cursor.fetchall()
        
        print("List of Authors:")
        for author in results:
            print(author)
    except Exception as e:
        print(f"Error displaying authors: {e}")
    finally:
        cursor.close()
        connection.close()
