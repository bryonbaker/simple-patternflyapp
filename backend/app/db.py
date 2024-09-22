import sqlite3
import os

DATABASE = 'customer.db'

# Function to delete and recreate the database with debug statements
def init_db():
    # Debug: Check if the database file exists and remove it
    if os.path.exists(DATABASE):
        print(f"Database '{DATABASE}' found, deleting it...")  # Debug statement
        os.remove(DATABASE)
    else:
        print(f"Database '{DATABASE}' not found, creating a new one...")  # Debug statement

    # Establish connection and create table
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    print("Creating 'customer' table...")  # Debug statement
    cursor.execute('''
        CREATE TABLE customer (
            cust_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            address TEXT NOT NULL,
            phone TEXT NOT NULL
        )
    ''')
    
    # Insert sample data
    sample_customers = [
        (1, "John Doe", "123 Main St", "123-456-7890"),
        (2, "Jane Smith", "456 Maple Ave", "987-654-3210"),
        (3, "Alice Johnson", "789 Oak Dr", "555-555-5555")
    ]
    
    print("Inserting sample customers...")  # Debug statement
    cursor.executemany("INSERT INTO customer (cust_id, name, address, phone) VALUES (?, ?, ?, ?)", sample_customers)

    # Commit and close connection
    conn.commit()
    print("Database initialized successfully with sample data.")  # Debug statement
    conn.close()

# Function to get a customer by ID
def get_customer_by_id(cust_id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    print(f"Searching for customer with ID {cust_id}...")  # Debug statement
    cursor.execute("SELECT * FROM customer WHERE cust_id=?", (cust_id,))
    customer = cursor.fetchone()
    
    conn.close()
    return customer
