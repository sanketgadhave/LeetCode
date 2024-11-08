# Write your MySQL query statement below
select 
visited_on,
(select sum(amount)
from customer
where visited_on BETWEEN DATE_SUB(C.visited_on, INTERVAL 6 DAY) AND C.visited_on) as Amount,
ROUND((select
sum(amount)/7 from customer
where visited_on BETWEEN DATE_SUB(C.visited_on, INTERVAL 6 DAY) AND C.visited_on),2) as average_amount

from Customer C
where visited_on >= (select DATE_ADD(MIN(visited_on), INTERVAL 6 DAY) from customer)
group by visited_on