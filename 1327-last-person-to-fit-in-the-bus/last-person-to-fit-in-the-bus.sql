-- Write your PostgreSQL query statement below
select res.person_name 
from (
select turn, person_id, person_name, weight,sum(weight) over(order by turn) as total_weight
from Queue) as res
where res.total_weight <= 1000
order by res.turn DESC limit 1