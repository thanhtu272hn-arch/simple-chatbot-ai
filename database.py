import sqlite3
import os

DB_FILE = os.path.join(os.getcwd(), "chat.db")

def get_conn():
    print("📂 CONNECT DB:", DB_FILE)
    return sqlite3.connect(DB_FILE, check_same_thread=False)


def init_db():
    conn = get_conn()
    cursor = conn.cursor()

    # 👇 bảng messages
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT,
        role TEXT,
        content TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # 👇 🔥 THÊM BẢNG NÀY
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_profile (
        user_id TEXT PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
    """)

    conn.commit()
    conn.close()