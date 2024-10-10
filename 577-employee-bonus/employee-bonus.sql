# Write your MySQL query statement below
select name, bonus from Employee emp left join Bonus B on emp.empId = B.empId where bonus is null or bonus < 1000