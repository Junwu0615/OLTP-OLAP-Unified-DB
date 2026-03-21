CREATE TABLE machine_events (
    event_id BIGSERIAL PRIMARY KEY,
    machine_id INT NOT NULL REFERENCES machines(machine_id),
    event_type VARCHAR(50), -- ERROR / MAINTENANCE
    severity INT,
    description TEXT,
    event_time TIMESTAMP NOT NULL
);