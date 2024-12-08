def delete_book(book_id):
    """Видалення книги за її ID"""
    conn = connect_to_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Books WHERE book_id = %s;", (book_id,))
            conn.commit()
            print(f"Книгу з ID {book_id} видалено.")
        except Exception as e:
            print(f"Помилка виконання запиту: {e}")
        finally:
            cursor.close()
            conn.close()

