/*
Enter your query here.
*/
with pt as (
select hacker_id, count(*) cnt
from challenges 
group by 1
)
select 
pt.hacker_id,h.name,  pt.cnt
from pt 
left join hackers h on h.hacker_id = pt.hacker_id
where cnt in (select max(cnt) cnt from pt) or cnt in (select cnt
    from pt 
    group by 1
    having count(*) = 1
)
order by pt.cnt desc, pt.hacker_id