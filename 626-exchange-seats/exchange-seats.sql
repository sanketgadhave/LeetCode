-- Write your PostgreSQL query statement below
with new as (
select id, student,
case when id%2 != 0 and id = (select max(id) from seat) then id
when id%2 !=0 and id != (select max(id) from seat) then id+1
else id-1 end as new_id
from Seat
order by new_id)

select new_id as id, student from new

