CREATE TABLE customers (
    customer_id INTEGER,
    first_name TEXT,
    last_name TEXT,
    birth_year INTEGER,
    registration_year INTEGER
);

CREATE TABLE contacts (
    contact_id INTEGER,
    customer_id INTEGER,
    email TEXT,
    phone TEXT
);

CREATE TABLE purchases (
    purchase_id INTEGER,
    customer_id INTEGER,
    purchase_year INTEGER,
    amount_rub INTEGER,
    product_type TEXT
);

