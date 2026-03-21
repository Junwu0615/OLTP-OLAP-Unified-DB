CREATE TABLE dim_time (
    time_key SERIAL PRIMARY KEY,
    timestamp TIMESTAMP,
    date DATE,
    hour INT,
    day INT,
    month INT,
    year INT,
    weekday INT
);