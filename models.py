import sqlite3

def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS quotes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        author TEXT NOT NULL,
        quote TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

def add_quote(author, quote):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO quotes (author, quote) VALUES (?, ?)', (author, quote))
    conn.commit()
    conn.close()

def get_random_quote():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT author, quote FROM quotes ORDER BY RANDOM() LIMIT 1')
    result = cursor.fetchone()
    conn.close()
    return result

def search_quotes_by_author(author):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT author, quote FROM quotes WHERE author LIKE ?', ('%' + author + '%',))
    results = cursor.fetchall()
    conn.close()
    return results
