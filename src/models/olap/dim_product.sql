CREATE TABLE dim_product (
    product_key SERIAL PRIMARY KEY,
    product_id INT,
    product_code VARCHAR(50),
    product_name VARCHAR(100)
);