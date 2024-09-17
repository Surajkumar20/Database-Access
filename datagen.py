import time
import random
import string
import psycopg2
from datetime import datetime

# PostgreSQL connection details
conn = psycopg2.connect(
    dbname="transactions",
    user="postgres",
    password="0",
    host="localhost",  # For local use 'localhost', for remote use IP
    port="6899"
)

# Create a cursor object using connection
cur = conn.cursor()

def generate_data():
    # Generate random data for each field
    user_id = random.randint(1000, 9999)
    user_email = ''.join(random.choices(string.ascii_lowercase, k=5)) + '@example.com'
    item_id = random.randint(100, 999)
    item_price = round(random.uniform(10.0, 100.0), 2)  # No-tax price
    date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    return user_id, user_email, item_id, item_price, date_time

def push_data_to_db():
    while True:
        user_id, user_email, item_id, item_price, date_time = generate_data()

        # Insert the generated data into the PostgreSQL database
        cur.execute("""
            INSERT INTO transactions (user_id, user_email, item_id, item_no_tax_price, transaction_time)
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (user_id) DO NOTHING
        """, (user_id, user_email, item_id, item_price, date_time))

        # Commit the transaction
        conn.commit()
        print(f"Inserted data: {user_id}, {user_email}, {item_id}, {item_price}, {date_time}")

        # Sleep for 2 seconds (0.5 Hz)
        time.sleep(2)

# Call the function to start pushing data
push_data_to_db()

# Close the cursor and connection when done
cur.close()
conn.close()