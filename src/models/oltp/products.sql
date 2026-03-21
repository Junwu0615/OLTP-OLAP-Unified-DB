CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    product_code VARCHAR(50) UNIQUE NOT NULL,
    product_name VARCHAR(100),
    standard_cycle_time_sec INT -- 每件理論時間
);