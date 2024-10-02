from db.database import get_connection  # Change here

class User:
    def __init__(self, name, library_id):
        self.name = name
        self.library_id = library_id
    
    def save(self):
        """Save user to the database."""
        try:
            connection = get_connection()  # Change here
            with connection.cursor() as cursor:
                query = "INSERT INTO users (name, library_id) VALUES (%s, %s)"
                cursor.execute(query, (self.name, self.library_id))
                connection.commit()
            print(f"User '{self.name}' added successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            connection.close()
    
    @staticmethod
    def get_all():
        """Retrieve all users from the database."""
        users = []
        try:
            connection = get_connection()  # Change here
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM users")
                results = cursor.fetchall()
                for row in results:
                    users.append({
                        "id": row[0],
                        "name": row[1],
                        "library_id": row[2]
                    })
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            connection.close()
        return users
