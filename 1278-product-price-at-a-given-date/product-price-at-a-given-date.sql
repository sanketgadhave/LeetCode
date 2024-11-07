-- Write your PostgreSQL query statement below
with max as (
select product_id, max(change_date) as max_date
from Products 
where change_date <= '2019-08-16'
group by product_id)

select P.product_id, P.new_price as price 
from Products p inner join max m
on P.product_id = m.product_id
and P.change_date = m.max_date
union
select product_id, 10 as price
from products 
where product_id not in (select product_id from max)