def add_book(title, author, genre, price, stock_quantity, supplier_id):
    """Додавання нової книги до таблиці"""
    conn = connect_to_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO Books (title, author, genre, price, stock_quantity, supplier_id)
                VALUES (%s, %s, %s, %s, %s, %s);
                """,
                (title, author, genre, price, stock_quantity, supplier_id)
            )
            conn.commit()
            print("Книгу додано успішно!")
        except Exception as e:
            print(f"Помилка виконання запиту: {e}")
        finally:
            cursor.close()
            conn.close()
