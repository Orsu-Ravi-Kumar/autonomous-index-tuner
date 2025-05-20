-- Drop the table if it already exists
IF OBJECT_ID('tempdb..simulated_backup_logs') IS NOT NULL
    DROP TABLE tempdb..simulated_backup_logs;

-- Recreate the simulated backup logs
SELECT TOP 100
    'TestDB' AS database_name,
    DATEADD(MINUTE, -10 * ROW_NUMBER() OVER (ORDER BY (SELECT NULL)), GETDATE()) AS backup_start_date,
    DATEADD(MINUTE, -10 * ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) + 5, GETDATE()) AS backup_finish_date,
    ABS(CHECKSUM(NEWID())) % 100000000 AS backup_size,
    'D' AS backup_type,
    ABS(CHECKSUM(NEWID())) % 1800 + 60 AS duration_seconds
INTO tempdb..simulated_backup_logs
FROM sys.all_objects a
CROSS JOIN sys.all_objects b;
SELECT * FROM tempdb..simulated_backup_logs;
