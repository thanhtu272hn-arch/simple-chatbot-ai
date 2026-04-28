from database import get_conn


def save_message(user_id, role, content):
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO messages (user_id, role, content)
        VALUES (?, ?, ?)
    """, (user_id, role, content))

    conn.commit()
    conn.close()


def load_history(user_id):
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT role, content
        FROM messages
        WHERE user_id = ?
        ORDER BY id
    """, (user_id,))

    rows = cursor.fetchall()
    conn.close()

    return [
        {"role": r[0], "content": r[1]}
        for r in rows
    ]


def clear_history(user_id):
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM messages WHERE user_id = ?", (user_id,))
    conn.commit()
    conn.close()


def get_profile(user_id):
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT name, age FROM user_profile WHERE user_id = ?
    """, (user_id,))

    row = cursor.fetchone()
    conn.close()

    if row:
        return {"name": row[0], "age": row[1]}
    return {"name": None, "age": None}


def save_profile(user_id, name=None, age=None):
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO user_profile (user_id, name, age)
        VALUES (?, ?, ?)
        ON CONFLICT(user_id) DO UPDATE SET
            name = COALESCE(?, name),
            age = COALESCE(?, age)
    """, (user_id, name, age, name, age))

    conn.commit()
    conn.close()
