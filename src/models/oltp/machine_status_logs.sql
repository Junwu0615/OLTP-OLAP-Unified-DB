CREATE TABLE machine_status_logs (
    log_id BIGSERIAL,
    machine_id INT NOT NULL,
    status VARCHAR(20),
    event_time TIMESTAMP NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) PARTITION BY RANGE (event_time);