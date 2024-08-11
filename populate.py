import sqlite3

# Connect to the database
conn = sqlite3.connect('models.py')
cursor = conn.cursor()

# List of quotes to be added
quotes = [
    ("Albert Einstein", "Life is like riding a bicycle. To keep your balance you must keep moving."),
    ("Mahatma Gandhi", "Be the change that you wish to see in the world."),
    ("Oscar Wilde", "Be yourself; everyone else is already taken."),
    ("Mark Twain", "The secret of getting ahead is getting started."),
    ("Eleanor Roosevelt", "The future belongs to those who believe in the beauty of their dreams."),
    ("Confucius", "It does not matter how slowly you go as long as you do not stop."),
    ("Nelson Mandela", "It always seems impossible until it’s done."),
    ("Steve Jobs", "Your time is limited, so don’t waste it living someone else’s life."),
    ("Dr. Seuss", "Don't cry because it's over, smile because it happened."),
    ("Marilyn Monroe", "I'm selfish, impatient, and a little insecure. I make mistakes, I am out of control, and at times hard to handle. But if you can't handle me at my worst, then you sure as hell don't deserve me at my best."),
]

# Insert the quotes into the database
for author, quote in quotes:
    cursor.execute('INSERT INTO quotes (author, quote) VALUES (?, ?)', (author, quote))

# Commit the transaction and close the connection
conn.commit()
conn.close()

print("Quotes added to the database successfully.")
