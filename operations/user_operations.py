from db.database import get_connection
from models.user import User

def add_user(name, library_id):
    """Add a new user to the database."""
    connection = get_connection()
    cursor = connection.cursor()
    
    try:
        query = """
        INSERT INTO users (name, library_id)
        VALUES (%s, %s)
        """
        cursor.execute(query, (name, library_id))
        connection.commit()
        print("User added successfully.")
    except Exception as e:
        print(f"Error adding user: {e}")
    finally:
        cursor.close()
        connection.close()


def view_user_details(user_id):
    """View details of a specific user by ID."""
    connection = get_connection()
    cursor = connection.cursor()
    
    try:
        query = "SELECT * FROM users WHERE id = %s"
        cursor.execute(query, (user_id,))
        result = cursor.fetchone()
        return result
    except Exception as e:
        print(f"Error fetching user details: {e}")
    finally:
        cursor.close()
        connection.close()


def display_all_users():
    """Display all users in the database."""
    connection = get_connection()
    cursor = connection.cursor()
    
    try:
        query = "SELECT * FROM users"
        cursor.execute(query)
        results = cursor.fetchall()
        
        print("List of Users:")
        for user in results:
            print(user)
    except Exception as e:
        print(f"Error displaying users: {e}")
    finally:
        cursor.close()
        connection.close()
