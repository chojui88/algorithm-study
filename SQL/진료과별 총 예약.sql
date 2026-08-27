select mcdp_cd as '진료과 코드', count(*) as '5월 예약 건수'
from appointment
where apnt_ymd like '2022-05%'
group by mcdp_cd
order by 2 asc, 1 asc