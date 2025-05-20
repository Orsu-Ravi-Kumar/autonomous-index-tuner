SELECT 
    mid.database_id,
    mid.object_id,
    migs.avg_total_user_cost,
    migs.avg_user_impact,
    migs.user_seeks,
    mid.equality_columns,
    mid.inequality_columns,
    mid.included_columns
FROM sys.dm_db_missing_index_groups mig
INNER JOIN sys.dm_db_missing_index_group_stats migs ON migs.group_handle = mig.index_group_handle
INNER JOIN sys.dm_db_missing_index_details mid ON mig.index_handle = mid.index_handle;
