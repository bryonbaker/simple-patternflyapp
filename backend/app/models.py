import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('customer.db')
cursor = conn.cursor()

# Create a table if not exists
cursor.execute('''CREATE TABLE IF NOT EXISTS customer (
    cust_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    address TEXT NOT NULL,
    phone TEXT NOT NULL
)''')

# Commit and close the connection
conn.commit()
conn.close()
