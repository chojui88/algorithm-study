select ID, 
case --내림차순으로 정렬
    when percent_rank() over (order by SIZE_OF_COLONY desc) <= 0.25 then 'CRITICAL'
    when percent_rank() over (order by SIZE_OF_COLONY desc) <= 0.5 then 'HIGH'
    when percent_rank() over (order by SIZE_OF_COLONY desc) <= 0.75 then 'MEDIUM'
    when percent_rank() over (order by SIZE_OF_COLONY desc) <= 1 then 'LOW'
END as COLONY_NAME
from ecoli_data
order by ID