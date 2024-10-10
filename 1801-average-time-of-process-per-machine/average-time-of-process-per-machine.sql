# Write your MySQL query statement below
with process_time as (
SELECT 
    machine_id, 
    process_id, 
    MAX(CASE WHEN activity_type = 'end' THEN timestamp END) - MAX(CASE WHEN activity_type = 'start' THEN timestamp END) AS processing_time
  FROM Activity
  GROUP BY machine_id, process_id)

select machine_id, ROUND(AVG(processing_time),3) as processing_time from process_time group by machine_id