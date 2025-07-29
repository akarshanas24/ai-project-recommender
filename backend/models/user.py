import sqlite3
import os

def create_user_table():
    # Make sure the db directory exists
    os.makedirs('db', exist_ok=True)
    
    conn = sqlite3.connect('db/database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

print("✅ user.py loaded successfully!")
