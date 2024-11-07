-- Write your PostgreSQL query statement below
select employee_id 
from Employees
where salary < 30000
and 
manager_id not in (select distinct employee_id from employees)
order by employee_id