# Write your MySQL query statement below
select product_name, unit_sold as unit from
(
select product_id, sum(unit) as unit_sold
from orders
where order_date >= '2020-02-01' and order_date <= '2020-02-29'
group by product_id
having unit_sold >= 100) as res
inner join
Products P
on res.product_id = P.product_id