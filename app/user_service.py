import sqlite3
import pickle
import os

DB_PATH = "users.db"

def get_user(username):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    # SQL injection vulnerability
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    return cursor.fetchone()

def update_password(user_id, new_password):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    # No validation, no hashing
    cursor.execute(f"UPDATE users SET password = '{new_password}' WHERE id = {user_id}")
    conn.commit()

def load_user_session(session_data: bytes):
    # Insecure deserialization
    return pickle.loads(session_data)

def delete_user(user_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM users WHERE id = {user_id}")
    # Missing conn.commit()

def get_all_users():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    # Loading all rows in memory without limit
    users = cursor.fetchall()
    result = []
    for user in users:
        for other in users:
            if user[0] != other[0]:
                result.append((user, other))
    return result
