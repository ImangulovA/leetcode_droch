-- 3156. Employee Task Duration and Concurrent Tasks
with taskoverlap as (
select t2.task_id secondary_task, extract(epoch from t.end_time-t.start_time) duration,
extract(epoch from t2.end_time-t.start_time) overlap, t.*
from tasks t
left join tasks t2 on t.start_time >= t2.start_time and t.start_time < t2.end_time and t.employee_id = t2.employee_id and t.task_id <> t2.task_id
),
tc as (select task_id, employee_id, count(distinct secondary_task) + 1 as tasks_combined
from taskoverlap
group by 1,2),
mct as (
select employee_id, max(tasks_combined) as max_concurrent_tasks
from tc
group by 1
),
tth as (
select employee_id, floor((sum(coalesce(duration,0)) - sum(coalesce(overlap,0)))/3600) total_task_hours
from taskoverlap
group by 1)
select * from tth
left join mct using (employee_id)
order by 1