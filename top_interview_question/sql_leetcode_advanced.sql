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

