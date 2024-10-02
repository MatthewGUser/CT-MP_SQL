from db.database import get_connection

class Book:
    def __init__(self, title, author_id, isbn, publication_date):
        self.title = title
        self.author_id = author_id
        self.isbn = isbn
        self.publication_date = publication_date
        self.availability = True  # Default to available

    def save(self):
        """Save book to the database."""
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                query = "INSERT INTO books (title, author_id, isbn, publication_date, availability) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(query, (self.title, self.author_id, self.isbn, self.publication_date, self.availability))
                connection.commit()
            print(f"Book '{self.title}' added successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            connection.close()

    @staticmethod
    def get_all():
        """Retrieve all books from the database."""
        books = []
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM books")
                results = cursor.fetchall()
                for row in results:
                    books.append({
                        "id": row[0],
                        "title": row[1],
                        "author_id": row[2],
                        "isbn": row[3],
                        "publication_date": row[4],
                        "availability": row[5]
                    })
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            connection.close()
        return books
