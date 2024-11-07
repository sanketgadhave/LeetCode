# Write your MySQL query statement below
select res.employee_id, res.name, count(res.reports) as reports_count, Round(avg(res.age)) as average_age 
from (select e1.employee_id, e1.name, e2.age, e2.name as reports 
from employees e1 inner join employees e2
on e1.employee_id = e2.reports_to) as res
group by res.employee_id, res.name
order by res.employee_id