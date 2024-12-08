import psycopg2
from .config import DB_CONFIG


def connect_to_db():
    """Функція для підключення до бази даних"""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except Exception as e:
        print(f"Помилка підключення до бази даних: {e}")
        return None