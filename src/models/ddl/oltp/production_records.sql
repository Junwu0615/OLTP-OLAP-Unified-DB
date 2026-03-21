CREATE TABLE production_records (
    record_id BIGSERIAL PRIMARY KEY,
    machine_id INT NOT NULL REFERENCES machines(machine_id),
    order_id INT NOT NULL REFERENCES production_orders(order_id),
    produced_qty INT NOT NULL,
    defect_qty INT DEFAULT 0,
    record_time TIMESTAMP NOT NULL
);