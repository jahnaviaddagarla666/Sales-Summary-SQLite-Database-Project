import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta

# Create connection to SQLite database
conn = sqlite3.connect('sales_data.db')
cursor = conn.cursor()

# Create sales table
cursor.execute('''
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    price REAL NOT NULL,
    sale_date DATE NOT NULL,
    customer_id INTEGER
)
''')

# Sample sales data
sales_data = [
    ('Laptop', 5, 999.99, '2024-01-15', 101),
    ('Mouse', 25, 29.99, '2024-01-16', 102),
    ('Keyboard', 15, 79.99, '2024-01-17', 103),
    ('Monitor', 8, 299.99, '2024-01-18', 104),
    ('Laptop', 3, 999.99, '2024-01-19', 105),
    ('Mouse', 30, 29.99, '2024-01-20', 106),
    ('Headphones', 12, 149.99, '2024-01-21', 107),
    ('Keyboard', 10, 79.99, '2024-01-22', 108),
    ('Monitor', 6, 299.99, '2024-01-23', 109),
    ('Laptop', 7, 999.99, '2024-01-24', 110),
    ('Tablet', 20, 399.99, '2024-01-25', 111),
    ('Headphones', 18, 149.99, '2024-01-26', 112),
    ('Mouse', 40, 29.99, '2024-01-27', 113),
    ('Tablet', 15, 399.99, '2024-01-28', 114),
    ('Monitor', 4, 299.99, '2024-01-29', 115)
]

# Insert data only if table is empty (optional safety)
cursor.execute("SELECT COUNT(*) FROM sales")
if cursor.fetchone()[0] == 0:
    cursor.executemany('''
    INSERT INTO sales (product, quantity, price, sale_date, customer_id)
    VALUES (?, ?, ?, ?, ?)
    ''', sales_data)

# Commit changes
conn.commit()

# Run query while connection is open
query = '''
SELECT product, SUM(quantity) AS total_qty, SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
'''

# Load the result into a pandas DataFrame
df = pd.read_sql_query(query, conn)

# Close the connection
conn.close()

# Show the summary table
print(df.head())

# Plot a simple bar chart of revenue by product
plt.figure(figsize=(8, 5))
plt.bar(df['product'], df['revenue'], color='skyblue')
plt.xlabel('Product')
plt.ylabel('Total Revenue ($)')
plt.title('Total Revenue by Product')
plt.tight_layout()
plt.savefig('sales_chart.png')
plt.show()

print('Bar chart of total revenue by product displayed and saved as sales_chart.png.')
