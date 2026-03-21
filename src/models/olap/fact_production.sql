CREATE TABLE fact_production (
    fact_id BIGSERIAL PRIMARY KEY,
    machine_key INT,
    product_key INT,
    time_key INT,
    produced_qty INT,
    defect_qty INT
);