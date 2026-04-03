SELECT aid % 10 AS machine_id, COUNT(*), AVG(abalance)
FROM pgbench_accounts
WHERE abalance >= 0
GROUP BY 1
ORDER BY 1;