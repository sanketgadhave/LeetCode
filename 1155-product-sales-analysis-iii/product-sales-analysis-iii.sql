# Write your MySQL query statement below
with first_year as (
    select product_id, min(year) as first_year from Sales group by product_id
)

select p.product_id, first_year, quantity, price 
from first_year p 
left join Sales s 
on p.product_id = s.product_id
where first_year = year