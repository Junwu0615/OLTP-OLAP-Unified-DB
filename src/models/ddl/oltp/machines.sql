CREATE TABLE machines (
    machine_id SERIAL PRIMARY KEY,
    machine_code VARCHAR(50) UNIQUE NOT NULL,
    machine_type VARCHAR(50) NOT NULL,
    location VARCHAR(100),
    status VARCHAR(20) NOT NULL, -- RUNNING / IDLE / DOWN
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);