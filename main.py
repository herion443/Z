import psycopg2

# Налаштування підключення до бази даних
connection = psycopg2.connect(
    host="localhost",       # Адреса сервера
    database="bookstore",   # Назва бази даних
    user="postgres",        # Ім'я користувача PostgreSQL
    password="5002",    # Пароль користувача
    port=5432               # Порт PostgreSQL (за замовчуванням 5432)
)

# Створення курсора для виконання SQL-запитів
cursor = connection.cursor()

# Виконання SQL-запиту: отримання всіх книг
try:
    cursor.execute("SELECT * FROM Books;")
    books = cursor.fetchall()

    print("Список книг:")
    for book in books:
        print(f"ID: {book[0]}, Назва: {book[1]}, Автор: {book[2]}, Жанр: {book[3]}, Ціна: {book[4]}, Кількість: {book[5]}")
except Exception as e:
    print(f"Помилка: {e}")

# Закриття підключення
finally:
    cursor.close()
    connection.close()
