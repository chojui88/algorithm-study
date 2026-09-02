select HOUR(datetime)as HOUR , count(*) as COUNT
from animal_outs
where HOUR(datetime) between 9 and 20
group by HOUR(datetime)
order by HOUR

--새롭게 알게된 것: 19:59 시간대는 HOUR(19) 쓰면 됨 x20