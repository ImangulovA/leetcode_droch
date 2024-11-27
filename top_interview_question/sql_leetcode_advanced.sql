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