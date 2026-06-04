-- 3103. Find Trending Hashtags II
with pt as (select string_to_table(tweet, ' ') words
from tweets)
select words as hashtag, count(*) as count
from pt
where left(words,1) = '#'
group by 1
order by 2 desc, 1 desc
limit 3