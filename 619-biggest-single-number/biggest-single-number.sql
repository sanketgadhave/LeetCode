# Write your MySQL query statement below
with large_count as (
    select num from MyNumbers group by num having count(1) = 1
)

select max(num) as num from large_count