import sqlite3

DB_FILE = "chat.db"

def get_conn():
    return sqlite3.connect(DB_FILE, check_same_thread=False)


def init_db():
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id TEXT,
    role TEXT,          -- "user" hoặc "bot"
    content TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
    """)

    conn.commit()
    conn.close()

