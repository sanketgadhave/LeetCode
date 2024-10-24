# Write your MySQL query statement below
with stud_count as (
    select class, count(distinct student) as stud_cnt from Courses group by class
)

select class from stud_count where stud_cnt >= 5