SELECT count(*) as Fish_count, month(time) as month
FROM FISH_INFO
group by month(time)
order by month