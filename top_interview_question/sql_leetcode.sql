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

# 1174. Immediate Food Delivery II
with fq as (
    select customer_id, min(order_date) order_date
    from Delivery
    group by 1
)
select round(100 * sum(order_date = customer_pref_delivery_date) / count(*),2) as immediate_percentage
from Delivery d
join fq using (customer_id,order_date)

# 550. Game Play Analysis IV
with pretable_a as (select player_id, min(event_date) as min_date
from activity a
group by player_id)
select round(sum(b.player_id is not null)/count(*),2) as fraction
from pretable_a pa
left join activity b on pa.player_id = b.player_id
and pa.min_date + interval 1 day = b.event_date

# 1141. User Activity for the Past 30 Days I
select activity_date day, count(distinct user_id) active_users
from activity
where activity_date <= '2019-07-27'
and activity_date > '2019-07-27' - interval 30 day
group by activity_date

# 1070. Product Sales Analysis III
with pretable as (select
product_id, min(year) year
from Sales
group by product_id)
select  s.product_id, s.year first_year, s.quantity, s.price
from Sales s
join pretable p using(product_id, year)

# 596. Classes More Than 5 Students
select class
from courses
group by class
having count(distinct student) >= 5


# 1729. Find Followers Count
select user_id, count(distinct follower_id) followers_count
from Followers
group by 1

# 619. Biggest Single Number
with uniq as
(select num
from MyNumbers
group by num
having count(*) = 1)
select max(num) num
from uniq

# 1045. Customers Who Bought All Products
select customer_id
from Customer
group by customer_id
having count(distinct product_key) = (select count(distinct product_key) from Product)


# 1731. The Number of Employees Which Report to Each Employee
with mantable as (
    select reports_to employee_id, count(*) reports_count, round(avg(age),0) average_age
    from employees
    where reports_to is not null
    group by reports_to
)
select e.employee_id, e.name, reports_count, average_age
from employees e
join mantable using(employee_id)
order by e.employee_id

# 180. Consecutive Numbers
select l0.num ConsecutiveNums
from logs l0
join logs l1 on l0.id = l1.id - 1
join logs l2 on l0.id = l2.id - 2
where l0.num = l1.num and l0.num = l2.num
group by 1

# 1204. Last Person to Fit in the Bus
with pt as (
select turn, weight, sum(weight) over (order by turn) sw
from Queue
)
select person_name
from queue
where turn = (select max(turn)
from pt
where sw <= 1000
)

# 1907. Count Salary Categories
select "Low Salary" as category, sum(case when income < 20000 then 1 else 0 end) as accounts_count
From Accounts
union
select "Average Salary" as category, sum(case when income between 20000 and 50000 then 1 else 0 end) as accounts_count
From Accounts
union
select "High Salary" as category, sum(case when income > 50000 then 1 else 0 end) as accounts_count
from Accounts

# 1978. Employees Whose Manager Left the Company
select e.employee_id
from Employees e
left join Employees m on e.manager_id = m.employee_id
where e.manager_id is not null
and m.employee_id is null
and e.salary < 30000

# 1321. Restaurant Growth
with pt as
(
    select visited_on, sum(amount) sa, count(*) ca, 1 techcol
    from customer
    group by visited_on
), pt2 as
(
select visited_on, sum(sa) over w amount,
round(sum(sa) over w/7,2) average_amount
from pt
window w as (
    ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND 0 FOLLOWING
    )
)
select *
from pt2
where visited_on > (
    select min(visited_on)+ interval 5 day
    from customer
    )

# 602. Friend Requests II: Who Has the Most Friends
WITH cte AS (
SELECT requester_id as id, COUNT(requester_id) as count
FROM RequestAccepted
GROUP BY requester_id
UNION ALL
SELECT accepter_id as id, COUNT(accepter_id) as count
FROM RequestAccepted
GROUP BY accepter_id
)
SELECT id, SUM(count) as num
FROM cte
GROUP BY id
ORDER BY num DESC
LIMIT 1;

# 585. Investments in 2016
with ul as
(
    select lat, lon
 from Insurance
 group by 1,2
 having count(*) = 1
),  ct as
(
    select tiv_2015
    from Insurance
    group by 1
    having count(*) > 1
)
select round(sum(tiv_2016),2) tiv_2016
from Insurance
join ul using(lat,lon)
join ct using(tiv_2015)

# 185. Department Top Three Salaries
with pt as
(
    select departmentId, salary, rank() over (partition by departmentId order by salary desc) srank
    from Employee
    group by 1,2
)
select d.name Department, e.name Employee, e.salary
from Employee e
join pt using (departmentId, salary)
join Department d on d.id = e.departmentId
where pt.srank <= 3

# 1527. Patients With a Condition
select *
from patients
where left(conditions,5) = 'DIAB1' or conditions like '% DIAB1%'

# 196. Delete Duplicate Emails

with pt as (
    select id, email, rank() over (partition by email order by id asc) srank
from person
)
delete
from person
where id in (select id from pt where srank > 1)

# 176. Second Highest Salary
with pt as
(
    select salary, rank() over (order by salary desc) srank
    from (select salary from Employee group by 1) e
)
select salary SecondHighestSalary
from pt
where srank = 2
union
select null SecondHighestSalary
limit 1

_____

select max(salary) as SecondHighestSalary from Employee
where salary <(select max(salary) from employee);

