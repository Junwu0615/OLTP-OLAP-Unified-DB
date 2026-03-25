DO $$
DECLARE
    start_time DATE;
    end_time DATE;
    schema_mode TEXT;
    table_name TEXT;
    target_name TEXT;
BEGIN
    schema_mode := 'oltp';
    target_name := 'machine_status_logs';

    start_time := date_trunc('month', CURRENT_DATE);
    end_time := start_time + interval '1 month';
    table_name := target_name || '_' || to_char(start_time, 'YYYY_MM');

    EXECUTE format(
        'CREATE TABLE IF NOT EXISTS %I.%I
        PARTITION OF %I.%I
        FOR VALUES FROM (%L) TO (%L)',
        schema_mode,
        table_name,
        schema_mode,
        target_name,
        start_time,
        end_time
    );

END $$;