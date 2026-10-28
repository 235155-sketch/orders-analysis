import sqlite3

conn = sqlite3.connect("orders.db")
cur = conn.cursor()

cur.executescript("""
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS customers;
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT,
    city TEXT
);
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    amount INTEGER,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);
INSERT INTO customers VALUES
(1, 'Ali', 'Islamabad'),
(2, 'Sara', 'Lahore'),
(3, 'Bilal', 'Islamabad'),
(4, 'Ayesha', 'Karachi'),
(5, 'Hamza', 'Lahore'),
(6, 'Zara', 'Rawalpindi');
INSERT INTO orders VALUES
(1, 1, 4500),
(2, 1, 7200),
(3, 2, 3000),
(4, 3, 9800),
(5, 4, 2500),
(6, 5, 8600),
(7, 5, 5200),
(8, 6, 1800),
(9, 2, 6000),
(10, 4, 3500);
""")

conn.commit()
conn.close()
print("Database created.")
