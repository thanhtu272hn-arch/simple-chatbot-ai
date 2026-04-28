import sqlite3

DB_FILE = "chat.db"

def get_conn():
    return sqlite3.connect(DB_FILE, check_same_thread=False)


def init_db():
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_profile (
    user_id TEXT PRIMARY KEY,
    name TEXT,
    age INTEGER
);
    """)

    conn.commit()
    conn.close()

