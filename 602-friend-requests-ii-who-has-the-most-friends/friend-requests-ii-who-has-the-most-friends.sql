# Write your MySQL query statement below
with accepted as (
select user_id as id, count(*) as num from
(select requester_id as user_id
from RequestAccepted
union all 
select accepter_id as user_id
from RequestAccepted) cte
group by user_id
)
select * from accepted where num = (select max(num) from accepted)