CREATE TABLE production_orders (
    order_id SERIAL PRIMARY KEY,
    product_id INT NOT NULL REFERENCES products(product_id),
    planned_qty INT NOT NULL,
    start_time TIMESTAMP,
    end_time TIMESTAMP,
    status VARCHAR(20), -- PLANNED / RUNNING / DONE
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);