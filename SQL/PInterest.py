'''
web_requests: date, user_id, browser [chrome, firefox, ie], request_count
api_requests: date, user_id, devide_type [iphone, ipad, android-phone], request_count

Goal: get the per-day count since the beginning of the year of users  who
visited at least one page on an iphone and the web on the same day
'''

'''
My solution (Baseline):

select web_requests.date, count(distinct web_requests.user_id) as users
from
web_requests
inner join
api_requests
on
web_requests.user_id=api_requests.user_id
and
web_requests.date=api_requests.date
where
web_requests.request_count >=1
and
api_requests.devide_type='iphone'
and
api_requests.request_count>=1;
and
web_requests.date >= '2019-01-01'
group by web_requests.date

Question: In both requests, there are multiple requests per user per day!

Better:
1. Find out in each table, those users with >=1 requests!

select t_web.date, count(t_web.user_id)

from

(select date, distinct user_id, count(request_count)
from web_requests
group by date, distinct user_id,
having count(request_count) >= 1
) as t_web

inner join

(select date, distinct user_id, count(request_count)
from web_requests
where devide_type='iphone'
grou by by date, distinct user_id
having count(request_count) > 1
) as t_api

where
t_web.user_id=t_api.user_id

group by t_web.date



# HAVING is evaluated after GROUP BY while WHERE is evaluated before!
https://stackoverflow.com/questions/41675073/sql-group-by-count-where-count-greater-than
'''


# Answer:
# select w.date, sum(w.request_count + a.request_count) from
# (select * from web_requests where date >= '2017-01-01') as w
# inner join
# (select * from api_requests where devide_type = "iphone" and date >= '2017-01-01') as a
# on w.date = a.date and w.user_id = a.user_id
# group by w.date


# select date, count(distinct user_id) as users
# from
# (
#     select date, user_id
# from api_request
# where device_type = 'iphone' and date >= '2019-01-01' and request_count > 0
#
#
# UNION
#
# select date, user_id
# from web_request
# where date >= '2019-01-01' and request_count > 0
# ) a
# group by date


# https://www.periscopedata.com/blog/use-subqueries-to-count-distinct-50x-faster




'''
Naive way:
- Workflow: Hash -> Join -> Sort -> Agg (DISTINCT COUNT) -> Sort

select 
  dashboards.name, 
  count(distinct time_on_site_logs.user_id)
from time_on_site_logs 
join dashboards on time_on_site_logs.dashboard_id = dashboards.id
group by name 
order by count desc


- Better: Agg (DISTINCT COUNT) -> Join -> Sort

select
  dashboards.name,
  log_counts.ct
from dashboards
join (
  select
    dashboard_id,
    count(distinct user_id) as ct
  from time_on_site_logs 
  group by dashboard_id
) as log_counts 
on log_counts.dashboard_id = dashboards.id
order by log_counts.ct desc


- Best: DISTINCT COUNT -> Agg -> Join -> Sort
# Count distinct builds a hash set for each group - in this 
# case, each dashboard_id - to keep track of which values have 
# been seen in which buckets.

# Instead of doing all that work, we can compute the distincts 
# in advance, which only needs one hash set. 

select
  dashboards.name,
  log_counts.ct
from dashboards 
join (
  select distinct_logs.dashboard_id, 
  count(1) as ct
  from (
    select distinct dashboard_id, user_id
    from time_on_site_logs
  ) as distinct_logs
  group by distinct_logs.dashboard_id
) as log_counts 
on log_counts.dashboard_id = dashboards.id
order by log_counts.ct desc



Really difference:
(select
    dashboard_id,
    count(distinct user_id) as ct
  from time_on_site_logs 
  group by dashboard_id)

(select distinct_logs.dashboard_id, 
  count(1) as ct
  from (
    select distinct dashboard_id, user_id
    from time_on_site_logs
  ) as distinct_logs
  group by distinct_logs.dashboard_id
)

We've taken the inner count-distinct-and-group and broken 
it up into two pieces. The inner piece computes distinct 
(dashboard_id, user_id) pairs. The second piece runs a simple, 
speedy group-and-count over them. As always, the join is last.  
'''
