from db.database import get_connection  # Change here

class BorrowedBook:
    def __init__(self, user_id, book_id, borrow_date, return_date=None):
        self.user_id = user_id
        self.book_id = book_id
        self.borrow_date = borrow_date
        self.return_date = return_date
    
    def save(self):
        """Save borrowed book record to the database."""
        try:
            connection = get_connection()  # Change here
            with connection.cursor() as cursor:
                query = "INSERT INTO borrowed_books (user_id, book_id, borrow_date, return_date) VALUES (%s, %s, %s, %s)"
                cursor.execute(query, (self.user_id, self.book_id, self.borrow_date, self.return_date))
                connection.commit()
            print("Borrowed book record added successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            connection.close()
    
    @staticmethod
    def get_all():
        """Retrieve all borrowed books from the database."""
        borrowed_books = []
        try:
            connection = get_connection()  # Change here
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM borrowed_books")
                results = cursor.fetchall()
                for row in results:
                    borrowed_books.append({
                        "id": row[0],
                        "user_id": row[1],
                        "book_id": row[2],
                        "borrow_date": row[3],
                        "return_date": row[4]
                    })
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            connection.close()
        return borrowed_books
