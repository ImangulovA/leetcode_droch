-- 1821. Find Customers With Positive Revenue this Year
select
customer_id
from customers
where year = 2021 and revenue > 0

-- 183. Customers Who Never Order
select name as customers
from customers
where id not in (select customerId from orders group by 1)

--1873. Calculate Special Bonus
select employee_id,
case when employee_id%2 = 1 and left(name,1) <> 'M' then salary
else 0 end as bonus
from employees
order by employee_id

-- 1398. Customers Who Bought Products A and B but Not C
with aborder as
(select customer_id from orders
where product_name in ('A', 'B')
group by 1
having count(distinct product_name) = 2)
select c.* from customers c
inner join aborder a using (customer_id)
where c.customer_id not in (select customer_id from orders
where product_name = 'C'
group by 1)
order by c.customer_id

-- 512. Game Play Analysis II
with pt as (select player_id, first_value(device_id) over(partition by player_id order by event_date) as device_id
from activity)
select *
from pt
group by 1,2
-- more optimal -- filter by time of first login

-- 1831. Maximum Transaction Each Day
with maxtransac as (select date(day) as day, max(amount) as amount
from transactions
group by 1)
select transaction_id
from transactions t
join maxtransac m on date(t.day) = m.day and t.amount=m.amount
order by 1

-- 607. Sales Person
with com as
(select com_id from company
where name = 'RED'),
comordsales as (
    select o.sales_id
    from orders o
    inner join com using (com_id)
    group by 1
)
select s.name from salesperson s
left join comordsales c using (sales_id)
where c.sales_id is null
-- not in subquery is more efficient

--1112. Highest Grade For Each Student
with pt as (select student_id, max(grade) as grade
from enrollments
group by 1)
select e.student_id, min(e.course_id) as course_id, e.grade
from enrollments e
inner join pt using(student_id, grade)
group by 1,3
order by student_id
-- row number / rank is WAY more efficient

--175. Combine Two Tables
select
p.firstname, p.lastname, a.city, a.state
from Person p
left join Address A using(personId)

-- 1412. Find the Quiet Students in All Exams
with minmax as (select exam_id, min(score) as min_score, max(score) as max_score
from exam
group by exam_id),
louddetect as (select e.exam_id, e.student_id,
case when e.score = mm.min_score or e.score = mm.max_score then True
else False end as loud
from exam e
join minmax mm using(exam_id)),
alwaysquiet as (select student_id, max(loud) ever_loud
from louddetect
group by 1)
select s.*
from student s
join alwaysquiet a using(student_id)
where a.ever_loud = 0

-- 1693. Daily Leads and Partners
select date_id, make_name, count(distinct lead_id) unique_leads,
count(distinct partner_id) unique_partners
from dailysales
group by 1,2

-- 1965. Employees With Missing Information
select coalesce(e.employee_id, s.employee_id) as employee_id
from employees e
full outer join salaries s using(employee_id)
where e.name is null or s.salary is null
order by 1

-- 184. Department Highest Salary
-- Write your PostgreSQL query statement below
with maxdep as (
    select departmentId, max(salary) salary from employee
    group by 1
)
select d.name as Department, e.name as Employee, e.salary
from employee e
inner join maxdep using(departmentId, salary)
inner join department d on d.id = e.departmentId

-- 1532. The Most Recent Three Orders
with orderrank as (select order_id, order_date, customer_id, rank() over(partition by customer_id order by order_date desc) orderrank
from orders
)
select c.name as customer_name, c.customer_id, o.order_id, o.order_date from
orderrank o
join customers c using(customer_id)
where o.orderrank <= 3
order by c.name, c.customer_id, o.order_date desc

-- 1445. Apples & Oranges
select sale_date,
sum(sold_num) filter(where fruit = 'apples')
- sum(sold_num) filter(where fruit = 'oranges') as diff
from sales
group by 1
order by 1

-- 1607. Sellers With No Sales
select seller_name
from seller
where seller_id not in (
select distinct seller_id from Orders
where extract(year from sale_date) = 2020
)
order by 1

-- 1747. Leetflex Banned Accounts
select distinct ip1.account_id
from LogInfo ip1
join LogInfo ip2 on ip1.account_id = ip2.account_id
and ip1.ip_address <> ip2.ip_address
and (
    --time cases
    (ip1.login >= ip2.login and ip1.login <= ip2.logout)
    OR
    (ip2.login >= ip1.login and ip2.login <= ip1.logout)
)

-- 1699. Number of Calls Between Two Persons
select
case when from_id < to_id then from_id
else to_id end as person1,
case when from_id > to_id then from_id
else to_id end as person2,
count(*) as call_count,
sum(duration) as total_duration
from calls
group by 1,2

-- 1077. Project Employees III
with most_years as
(
    select p.project_id, max(experience_years) experience_years
    from Employee e
    right join Project p using(employee_id)
    group by 1
)
select p.project_id, e.employee_id
from Project p
join most_years my using (project_id)
join employee e on p.employee_id = e.employee_id and e.experience_years = my.experience_years

-- 1596. The Most Frequently Ordered Products for Each Customer
with frequent_buy as (
    select customer_id, product_id, count(distinct order_id) num_of_orders from orders
    group by 1,2
),
most_often as
(
    select *, rank() over(partition by customer_id order by num_of_orders desc) burank
    from frequent_buy
)
select mo.customer_id, mo.product_id, p.product_name
from most_often mo
join products p using (product_id)
where mo.burank = 1

-- 1767. Find the Subtasks That Did Not Execute
with gentask as
(select subtask_id
from generate_series(1,20) subtask_id
)
select
task_id, subtask_id
from tasks
cross join gentask g
left join executed e using (task_id, subtask_id)
where g.subtask_id <= subtasks_count
and e.task_id is null

-- 603. Consecutive Available Seats
with free as (select seat_id
from cinema
where free = 1)
select f1.seat_id
from free f1
left join free f2 on f1.seat_id = f2.seat_id + 1
left join free f3 on f1.seat_id = f3.seat_id - 1
where f2.seat_id is not null or f3.seat_id is not null
order by f1.seat_id

-- 608. Tree Node
select t.id,
case when parent.id is null then 'Root'
when child.p_id is not null then 'Inner'
else 'Leaf' end as type
from tree t
left join tree parent on t.p_id = parent.id
left join (select distinct p_id from tree) child on t.id = child.p_id

-- 1890. The Latest Login in 2020
select user_id, max(time_stamp ) last_stamp
from logins
where extract(year from time_stamp) = 2020
group by 1

-- 1264. Page Recommendations
select
distinct page_id recommended_page
from
likes
where user_id in (select
    user2_id as user_id
    from friendship
    where user1_id = 1
    UNION
    select
    user1_id as user_id
    from friendship
    where user2_id = 1)
and page_id not in (
select page_id recommended_page
from
likes
where user_id = 1
)

-- 1709. Biggest Window Between Visits
with lead_windows as (
select user_id, visit_date,
coalesce(lead(visit_date, 1) over (partition by user_id order by visit_date), '2021-01-01') as next_v_day
from uservisits
)
select user_id, max(next_v_day - visit_date)  as biggest_window
from lead_windows
group by 1
order by 1