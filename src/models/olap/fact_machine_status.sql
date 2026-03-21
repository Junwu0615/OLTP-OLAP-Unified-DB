CREATE TABLE fact_machine_status (
    fact_id BIGSERIAL PRIMARY KEY,
    machine_key INT,
    time_key INT,
    running_seconds INT,
    idle_seconds INT,
    down_seconds INT
);