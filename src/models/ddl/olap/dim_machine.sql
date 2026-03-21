CREATE TABLE dim_machine (
    machine_key SERIAL PRIMARY KEY,
    machine_id INT,
    machine_code VARCHAR(50),
    machine_type VARCHAR(50),
    location VARCHAR(100)
);