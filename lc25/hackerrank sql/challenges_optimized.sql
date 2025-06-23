/*
Оптимизированная версия с оконными функциями
*/
with challenge_counts as (
    select 
        hacker_id,
        count(*) as cnt,
        max(count(*)) over () as max_count,
        count(*) over (partition by count(*)) as cnt_frequency
    from challenges 
    group by hacker_id
)
select 
    cc.hacker_id,
    h.name,  
    cc.cnt
from challenge_counts cc
left join hackers h on h.hacker_id = cc.hacker_id
where cc.cnt = cc.max_count 
   or cc.cnt_frequency = 1
order by cc.cnt desc, cc.hacker_id 