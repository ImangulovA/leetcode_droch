/*
Enter your query here.
*/
select cn.contest_id, cn.hacker_id, cn.name, sum(ss.total_submissions) total_submissions,
sum(ss.total_accepted_submissions) total_accepted_submissions,
sum(vs.total_views) total_views,
sum(vs.total_unique_views) total_unique_views
from contests cn
left join colleges cl on cl.contest_id = cn.contest_id
left join challenges cg on cg.college_id = cl.college_id
left join view_stats vs on vs.challenge_id = cg.challenge_id
left join submission_stats ss on ss.challenge_id = cg.challenge_id
group by 1,2,3
having sum(ss.total_submissions) +
sum(ss.total_accepted_submissions) +
sum(vs.total_views) +
sum(vs.total_unique_views) > 0
order by cn.contest_id;
