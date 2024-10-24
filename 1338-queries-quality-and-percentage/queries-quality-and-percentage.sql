# Write your MySQL query statement below
select query_name, Round(sum(rating/position) / count(*), 2) as quality, 
Round((count(case when rating < 3 then 1 end) * 100.0) / count(*), 2) as poor_query_percentage 
from Queries where query_name is not null
group by query_name