from flask import Flask, request, jsonify
from database.connect_to_db import connect_to_db


app = Flask(__name__)

# Маршрут для отримання всіх книг
@app.route('/books', methods=['GET'])
def get_books():
    """Отримати список усіх книг"""
    conn = connect_to_db()
    if not conn:
        return jsonify({"error": "Помилка підключення до бази даних"}), 500

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Books")
        books = cursor.fetchall()
        cursor.close()
        conn.close()

        books_list = [
            {
                "book_id": book[0],
                "title": book[1],
                "author": book[2],
                "genre": book[3],
                "price": float(book[4]),
                "stock_quantity": book[5],
                "supplier_id": book[6]
            }
            for book in books
        ]
        return jsonify(books_list), 200
    except Exception as e:
        return jsonify({"error": f"Помилка виконання запиту: {e}"}), 500

# Маршрут для додавання нової книги
@app.route('/books', methods=['POST'])
def add_book():
    """Додати нову книгу"""
    data = request.json
    conn = connect_to_db()
    if not conn:
        return jsonify({"error": "Помилка підключення до бази даних"}), 500

    try:
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO Books (title, author, genre, price, stock_quantity, supplier_id)
            VALUES (%s, %s, %s, %s, %s, %s)
            RETURNING book_id;
            """,
            (data['title'], data['author'], data['genre'], data['price'], data['stock_quantity'], data['supplier_id'])
        )
        new_book_id = cursor.fetchone()[0]
        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({"message": "Книгу додано успішно", "book_id": new_book_id}), 201
    except Exception as e:
        return jsonify({"error": f"Помилка виконання запиту: {e}"}), 500

# Маршрут для оновлення книги
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    """Оновити дані про книгу"""
    data = request.json
    conn = connect_to_db()
    if not conn:
        return jsonify({"error": "Помилка підключення до бази даних"}), 500

    try:
        cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE Books
            SET title = %s, author = %s, genre = %s, price = %s, stock_quantity = %s, supplier_id = %s
            WHERE book_id = %s;
            """,
            (data['title'], data['author'], data['genre'], data['price'], data['stock_quantity'], data['supplier_id'], book_id)
        )
        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({"message": "Книгу оновлено успішно"}), 200
    except Exception as e:
        return jsonify({"error": f"Помилка виконання запиту: {e}"}), 500

# Маршрут для видалення книги
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    """Видалити книгу за її ID"""
    conn = connect_to_db()
    if not conn:
        return jsonify({"error": "Помилка підключення до бази даних"}), 500

    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Books WHERE book_id = %s;", (book_id,))
        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({"message": "Книгу видалено успішно"}), 200
    except Exception as e:
        return jsonify({"error": f"Помилка виконання запиту: {e}"}), 500


# Запуск сервера
if __name__ == "__main__":
    app.run(debug=True)