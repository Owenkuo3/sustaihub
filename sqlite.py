import sqlite3

def create_database():
    conn = sqlite3.connect('news.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS news (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

create_database()

def save_to_database(titles):
    conn = sqlite3.connect('news.db')
    c = conn.cursor()
    for title in titles:
        c.execute('''
            INSERT INTO news (title) VALUES (?)
        ''', (title,))
    conn.commit()
    conn.close()
