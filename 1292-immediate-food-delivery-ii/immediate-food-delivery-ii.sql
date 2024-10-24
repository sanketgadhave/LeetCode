# Write your MySQL query statement below
with order_type as (
    select *, case when customer_pref_delivery_date = order_date then 'immediate' else 'scheduled' end as order_typ 
    from Delivery
),

ranked_orders AS (
    select * from (SELECT 
        customer_id, 
        delivery_id, 
        order_date,
        order_typ,
        ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date ASC) AS rn
    from order_type) e group by e.customer_id
)

select Round((count(case when order_typ = 'immediate' then 1 end) * 100)/count(*), 2) as immediate_percentage  
from ranked_orders
