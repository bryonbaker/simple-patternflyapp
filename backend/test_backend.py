import unittest
import sqlite3
import os
from app import create_app
from app.db import get_db_connection

class CustomerSearchTestCase(unittest.TestCase):
    def setUp(self):
        # Set up a temporary SQLite test database
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['DATABASE'] = 'test_customer.db'
        self.client = self.app.test_client()

        # Initialize the test database and add sample data
        with self.app.app_context():
            self.init_db()

    def tearDown(self):
        # Remove the test database after tests
        if os.path.exists('test_customer.db'):
            os.remove('test_customer.db')

    def init_db(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        # Create table
        cursor.execute('''CREATE TABLE customer (
            cust_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            address TEXT NOT NULL,
            phone TEXT NOT NULL
        )''')

        # Insert sample data
        cursor.execute("INSERT INTO customer (cust_id, name, address, phone) VALUES (1, 'John Doe', '123 Main St', '555-1234')")
        cursor.execute("INSERT INTO customer (cust_id, name, address, phone) VALUES (2, 'Jane Smith', '456 Oak Ave', '555-5678')")

        conn.commit()
        conn.close()

    def test_search_customer_found(self):
        # Test searching for an existing customer
        response = self.client.get('/search_customer?cust_id=1')
        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertEqual(data["cust_id"], 1)
        self.assertEqual(data["name"], 'John Doe')
        self.assertEqual(data["address"], '123 Main St')
        self.assertEqual(data["phone"], '555-1234')

    def test_search_customer_not_found(self):
        # Test searching for a non-existent customer
        response = self.client.get('/search_customer?cust_id=999')
        self.assertEqual(response.status_code, 404)

        data = response.get_json()
        self.assertEqual(data["error"], "Customer not found")

    def test_search_customer_no_id(self):
        # Test request without customer ID
        response = self.client.get('/search_customer')
        self.assertEqual(response.status_code, 400)

        data = response.get_json()
        self.assertEqual(data["error"], "No customer ID provided")


if __name__ == '__main__':
    unittest.main()
