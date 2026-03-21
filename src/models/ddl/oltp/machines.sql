CREATE TABLE oltp.machines (
    machine_id SERIAL PRIMARY KEY,
    machine_name VARCHAR(100) NOT NULL,
    machine_type VARCHAR(50),
    line_no VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE INDEX idx_machines_line
ON oltp.machines(line_no);