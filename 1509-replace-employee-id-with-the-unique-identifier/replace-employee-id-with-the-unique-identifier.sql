# Write your MySQL query statement below
select unique_id, name from Employees emp left join EmployeeUNI empU on emp.id = empU.id