# Write your MySQL query statement below
with top3_salaries as (
select * from (
select * , dense_rank() over(partition by departmentId  order by salary DESC) as rn
from Employee) as top3 where top3.rn <=3)

select D.name as Department, e1.name as Employee, e1.salary as Salary from (
select id, name, salary, departmentid
from employee e
where salary in (select salary from top3_salaries where departmentid = e.departmentid)
order by salary DESC) e1 left join
Department D
on e1.departmentid = D.id
