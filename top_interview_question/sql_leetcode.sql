# 197. Rising Temperature
SELECT w1.Id
FROM Weather w1, Weather w2
WHERE dateDiff(w1.recordDate,w2.recordDate) = 1 AND w1.Temperature > w2.Temperature;

# 1661. Average Time of Process per Machine
select s.machine_id, round(avg(e.timestamp-s.timestamp),3) as processing_time from activity as s
join activity as e on s.activity_type = 'start' and e.activity_type = 'end' and s.process_id = e.process_id and s.machine_id = e.machine_id
group by s.machine_id

# 577. Employee Bonus
select name, b.bonus
from employee
left join bonus b using(empId)
where b.bonus is null or b.bonus < 1000

# 1280. Students and Examinations
select s.student_id, s.student_name, su.subject_name, coalesce(ex.attended_exams,0) as attended_exams
from Students s
cross join Subjects su
left join (
    select student_id,subject_name,  count(*) as attended_exams
    from Examinations
    group by 1,2
) ex using(student_id, subject_name)
order by s.student_id, su.subject_name

# 570. Managers with at Least 5 Direct Reports
with pretable as
(
    select managerId
from employee
group by managerId
having count(distinct id) >= 5
)
select e.name
from Employee e
join pretable p on e.id = p.managerId

# 1934. Confirmation rate
with pretable as (
    select user_id, sum(action = 'confirmed') msg, count(*) all_msg
from confirmations
group by user_id
)
select s.user_id, case when p.user_id is null then 0 else round(p.msg/p.all_msg,2) end
as confirmation_rate
from signups s
left join pretable p using(user_id)

# 620. Not Boring Movies
select *
from cinema
where id%2 = 1 and description <> 'boring'
order by rating desc

# 1251. Average Selling Price
select p.product_id,
coalesce(round(sum(p.price*u.units)/sum(u.units),2),0) as average_price
from Prices p
left join UnitsSold u on u.product_id = p.product_id and u.purchase_date <= p.end_date and u.purchase_date >= p.start_date
group by product_id

# 1075. Project Employees I
select p.project_id, round(avg(e.experience_years),2)  as average_years
from Project p
left join Employee e using(employee_id)
group by p.project_id

# 1633. Percentage of Users Attended a Contest
with numall as (select count(*) numall from Users)
select contest_id, round(count(*)*100/numall,2) as percentage
from Register
join numall
group by contest_id
order by 2 desc, 1 asc

# 1211. Queries Quality and Percentage
select query_name, round(avg(rating/position),2) as quality, round(100*sum(rating<3)/count(*),2) as poor_query_percentage
from Queries
where query_name is not null
group by query_name

# 1193. Monthly Transactions I
select  DATE_FORMAT(trans_date, '%Y-%m') AS month, country,
count(*) trans_count,
sum(state = 'approved') approved_count,
sum(amount) trans_total_amount,
sum(amount * (state = 'approved')) approved_total_amount
from transactions
group by 1,2