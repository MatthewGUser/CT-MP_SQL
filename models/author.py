from db.database import get_connection  # Change here

class Author:
    def __init__(self, name, biography):
        self.name = name
        self.biography = biography
    
    def save(self):
        """Save author to the database."""
        try:
            connection = get_connection()  # Change here
            with connection.cursor() as cursor:
                query = "INSERT INTO authors (name, biography) VALUES (%s, %s)"
                cursor.execute(query, (self.name, self.biography))
                connection.commit()
            print(f"Author '{self.name}' added successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            connection.close()
    
    @staticmethod
    def get_all():
        """Retrieve all authors from the database."""
        authors = []
        try:
            connection = get_connection()  # Change here
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM authors")
                results = cursor.fetchall()
                for row in results:
                    authors.append({
                        "id": row[0],
                        "name": row[1],
                        "biography": row[2]
                    })
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            connection.close()
        return authors
