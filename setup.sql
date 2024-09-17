-- Create a database named 'transactions'
CREATE DATABASE transactions;

-- Connect to the transactions database
\connect transactions;

-- Create a table to hold transaction data
CREATE TABLE transactions (
    user_id SERIAL PRIMARY KEY,
    user_email VARCHAR(255) NOT NULL,
    item_id INT NOT NULL,
    item_no_tax_price DECIMAL(10, 2) NOT NULL,
    transaction_time TIMESTAMP NOT NULL,
    item_tax DECIMAL(10, 2) GENERATED ALWAYS AS (item_no_tax_price * 0.10) STORED
);